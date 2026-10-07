from __future__ import annotations

from datetime import date
from decimal import Decimal
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


class ProjectStatus(StrEnum):
    HEALTHY = "healthy"
    WATCH = "watch"
    AT_RISK = "at_risk"


class PersonStatus(StrEnum):
    AVAILABLE = "available"
    BUSY = "busy"
    OVERBOOKED = "overbooked"
    MISSING_TIME = "missing_time"


class Person(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=2, max_length=100)
    role: str = Field(min_length=2, max_length=100)
    daily_capacity_hours: Decimal = Field(default=Decimal("8"), ge=Decimal("0"), le=Decimal("24"))
    logged_hours_today: Decimal = Field(default=Decimal("0"), ge=Decimal("0"), le=Decimal("24"))

    @property
    def capacity_remaining(self) -> Decimal:
        return max(Decimal("0"), self.daily_capacity_hours - self.logged_hours_today)

    @property
    def status(self) -> PersonStatus:
        if self.logged_hours_today == Decimal("0"):
            return PersonStatus.MISSING_TIME
        if self.logged_hours_today > self.daily_capacity_hours:
            return PersonStatus.OVERBOOKED
        if self.capacity_remaining <= Decimal("2"):
            return PersonStatus.BUSY
        return PersonStatus.AVAILABLE


class Project(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=2, max_length=120)
    client: str = Field(min_length=2, max_length=120)
    budget_hours: Decimal = Field(gt=Decimal("0"))
    logged_hours: Decimal = Field(default=Decimal("0"), ge=Decimal("0"))
    delivery_date: date

    @field_validator("logged_hours")
    @classmethod
    def logged_hours_must_not_exceed_four_times_budget(
        cls, value: Decimal, info: object
    ) -> Decimal:
        budget_hours = getattr(info, "data", {}).get("budget_hours")
        if budget_hours is not None and value > budget_hours * Decimal("4"):
            raise ValueError("Logged hours exceed the permitted validation limit")
        return value

    @property
    def budget_remaining_hours(self) -> Decimal:
        return max(Decimal("0"), self.budget_hours - self.logged_hours)

    @property
    def budget_burn_percentage(self) -> Decimal:
        return (self.logged_hours / self.budget_hours * Decimal("100")).quantize(Decimal("0.1"))

    def days_until_delivery(self, today: date) -> int:
        return (self.delivery_date - today).days

    def status(self, today: date) -> ProjectStatus:
        days_remaining = self.days_until_delivery(today)
        burn = self.budget_burn_percentage
        if burn >= Decimal("100") or (days_remaining <= 5 and burn >= Decimal("80")):
            return ProjectStatus.AT_RISK
        if burn >= Decimal("60") or days_remaining <= 14:
            return ProjectStatus.WATCH
        return ProjectStatus.HEALTHY


class Workspace(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=2, max_length=120)
    projects: list[Project] = Field(default_factory=list)
    people: list[Person] = Field(default_factory=list)
    today: date = Field(default_factory=date.today)

    @property
    def total_budget_hours(self) -> Decimal:
        return sum((p.budget_hours for p in self.projects), Decimal("0"))

    @property
    def total_logged_hours(self) -> Decimal:
        return sum((p.logged_hours for p in self.projects), Decimal("0"))

    @property
    def overall_burn_percentage(self) -> Decimal:
        if self.total_budget_hours == Decimal("0"):
            return Decimal("0")
        return (self.total_logged_hours / self.total_budget_hours * Decimal("100")).quantize(
            Decimal("0.1")
        )


class Log(BaseModel):
    model_config = ConfigDict(frozen=True)

    person: str
    hours: Decimal
    date: date

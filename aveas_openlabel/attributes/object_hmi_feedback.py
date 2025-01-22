from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    NumberData,
    no_default,
)


@dataclass
class HmiFeedbackVisual(NumberData):
    """
        Numeric ID indicating some study-specific visual feedback given to the operator, e.g., via a warning light.
    A value of 0 means that no relevant visual feedback was given to the driver.
    Any value <> 0 denotes a study-specific feedback ID that must be specified in the study description document referenced in the acquisition’s resources field.
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: int = field(default_factory=lambda: no_default(field="HmiFeedbackVisual.val"), metadata=required)
    """Hmi_feedback visual value"""

    name: Literal["object/hmi_feedback/visual"] = field(default="object/hmi_feedback/visual")
    """Is always object/hmi_feedback/visual"""


@dataclass
class HmiFeedbackAcoustic(NumberData):
    """
        Numeric ID indicating some study-specific acoustic feedback given to the operator, e.g., via a warning sound.
    A value of 0 means that no relevant acoustic feedback was given to the driver.
    Any value <> 0 denotes a study-specific feedback ID that must be specified in the study description document referenced in the acquisition’s resources field.
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: int = field(default_factory=lambda: no_default(field="HmiFeedbackAcoustic.val"), metadata=required)
    """Hmi_feedback acoustic value"""

    name: Literal["object/hmi_feedback/acoustic"] = field(default="object/hmi_feedback/acoustic")
    """Is always object/hmi_feedback/acoustic"""


@dataclass
class HmiFeedbackOther(NumberData):
    """
        Numeric ID indicating some study-specific other feedback given to the operator, e.g. haptic feedback.
    A value of 0 means that no relevant other feedback was given to the driver.
    Any value <> 0 denotes a study-specific feedback ID that must be specified in the study description document referenced in the acquisition’s resources field.
    Measurement unit: (dimensionless)
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: int = field(default_factory=lambda: no_default(field="HmiFeedbackOther.val"), metadata=required)
    """Hmi_feedback other value"""

    name: Literal["object/hmi_feedback/other"] = field(default="object/hmi_feedback/other")
    """Is always object/hmi_feedback/other"""

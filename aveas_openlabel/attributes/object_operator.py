from dataclasses import dataclass, field
from typing import Literal

from apischema.metadata import required
from uai_openlabel import (
    Number,
    NumberData,
    ObjectUid,
    TextData,
    VectorData,
    no_default,
)


@dataclass
class OperatorAge(NumberData):
    """
        Age of the vehicle’s operator.
    Measurement unit: year
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: int = field(default_factory=lambda: no_default(field="OperatorAge.val"), metadata=required)
    """Operator age value"""

    name: Literal["object/operator/age"] = field(default="object/operator/age")
    """Is always object/operator/age"""


@dataclass
class OperatorGender(TextData):
    """
        Gender of the traffic participant or vehicle operator.
    Measurement unit: (dimensionless)
    Value range: (enumeration)
    Recommended distribution: probability vector
    Possible values:
     - FEMALE: female operator
     - MALE: male operator
     - DIVERSE: diverse operator
    """

    val: str = field(default_factory=lambda: no_default(field="OperatorGender.val"), metadata=required)
    """Operator gender value"""

    name: Literal["object/operator/gender"] = field(default="object/operator/gender")
    """Is always object/operator/gender"""


@dataclass
class OperatorBodyHeight(NumberData):
    """
        Body height of the vehicle operator.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="OperatorBodyHeight.val"), metadata=required)
    """Operator body_height value"""

    name: Literal["object/operator/body_height"] = field(default="object/operator/body_height")
    """Is always object/operator/body_height"""


@dataclass
class OperatorHeadDirection(NumberData):
    """
        Angle between head forward direction and forward direction of the vehicle, CCW.
    Measurement unit: rad
    Value range: (unbounded)
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="OperatorHeadDirection.val"), metadata=required)
    """Operator head_direction value"""

    name: Literal["object/operator/head_direction"] = field(default="object/operator/head_direction")
    """Is always object/operator/head_direction"""


@dataclass
class OperatorGazeDirection(NumberData):
    """
        Angle between gaze direction and forward direction of the vehicle, CCW.
    Measurement unit: rad
    Value range: [−π, π]
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="OperatorGazeDirection.val"), metadata=required)
    """Operator gaze_direction value"""

    name: Literal["object/operator/gaze_direction"] = field(default="object/operator/gaze_direction")
    """Is always object/operator/gaze_direction"""


@dataclass
class OperatorFocusedPoint(VectorData):
    """
        (x, y, z) coordinates of the focused point in vehicle coordinates, which shall be derived by extending the viewing beam from the operators’ eyes into the surrounding 3D world until it hits an object (other than the vehicle windows).
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: tuple[Number, Number, Number] = field(
        default_factory=lambda: no_default(field="OperatorFocusedPoint.val"), metadata=required
    )
    """Operator focused_point value"""

    name: Literal["object/operator/focused_point"] = field(default="object/operator/focused_point")
    """Is always object/operator/focused_point"""


@dataclass
class OperatorFocusedObjectType(TextData):
    """
        Type of object the operator is focusing on.
    Measurement unit: (dimensionless)
    Value range: (enumeration)
    Recommended distribution: probability vector
    Possible values:
     - LEADING_VEHICLE: Focused object is the vehicle in front of the operator
     - COLLIDING_VEHICLE: Focused object is a vehicle in the scene having a collision
     - GENERIC_VEHICLE: Focused object is a generic vehicle in the scene
     - SIGNAL: Focused object is a traffic signal
     - CENTER_DISPLAY: Focused object is the vehicle-inter center display
     - INSTRUMENT_CLUSTER: Focused object is the vehicle-inter instrument cluster
     - HUD: Focused object is the vehicle-inter head-up display
     - OTHER_DISPLAY: Focused object is another vehicle-inter head-up display
     - LEFT_MIRROR: Focused object is the left rear-view mirror
     - RIGHT_MIRROR: Focused object is the right rear-view mirror
     - CENTER_MIRROR: Focused object is the center rear-view mirror
     - CELL_PHONE: Focused object is a cell phone or other mobile device on the interior
     - OTHER_INTERIOR: Focused object is another object in the vehicle's interior (or on the vehicle's body)
     - OTHER_EXTERIOR: Focused object is another exterior object
    """

    val: str = field(default_factory=lambda: no_default(field="OperatorFocusedObjectType.val"), metadata=required)
    """Operator focused_object_type value"""

    name: Literal["object/operator/focused_object_type"] = field(default="object/operator/focused_object_type")
    """Is always object/operator/focused_object_type"""


@dataclass
class OperatorFocusedObjectId(TextData):
    """

    Measurement unit: (complex)
    Value range: (unbounded)
    Recommended distribution: (none)
    """

    val: ObjectUid = field(default_factory=lambda: no_default(field="OperatorFocusedObjectId.val"), metadata=required)
    """Operator focused_object_id value"""

    name: Literal["object/operator/focused_object_id"] = field(default="object/operator/focused_object_id")
    """Is always object/operator/focused_object_id"""


@dataclass
class OperatorDownvisionAngle(NumberData):
    """
        Operator’s eye viewing angle between the horizon and the closest point of the road / ground visible in the operator's field of view at zero heading, below which the vehicle’s hood or cowl blocks the field of view. See Parkinson and Reed, “Optimizing Vehicle Occupant Packaging”.
    Measurement unit: rad
    Value range: [0, π/2]
    Recommended distribution: rectangular
    """

    val: float = field(default_factory=lambda: no_default(field="OperatorDownvisionAngle.val"), metadata=required)
    """Operator downvision_angle value"""

    name: Literal["object/operator/downvision_angle"] = field(default="object/operator/downvision_angle")
    """Is always object/operator/downvision_angle"""


@dataclass
class OperatorViewingHeight(NumberData):
    """
        Operator's eye height above the road surface.
    Measurement unit: m
    Value range: (unbounded)
    Recommended distribution: normal
    """

    val: float = field(default_factory=lambda: no_default(field="OperatorViewingHeight.val"), metadata=required)
    """Operator viewing_height value"""

    name: Literal["object/operator/viewing_height"] = field(default="object/operator/viewing_height")
    """Is always object/operator/viewing_height"""


@dataclass
class OperatorSaliency(VectorData):
    """
        The saliency indicates salient objects in the operator’s field of view. The field of view is divided into 16 bins. Each bin contains a value from 0 to 1. 0 indicates the absence of a salient object. 1 indicates the presence of a salient object, e.g., an alarm signal, a catchy billboard or an unexpected oncoming object.
    Measurement unit: (dimensionless)
    Value range: [0.0, 1.0]
    Recommended distribution: (none)
    """

    val: tuple[
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
        Number,
    ] = field(default_factory=lambda: no_default(field="OperatorSaliency.val"), metadata=required)
    """Operator saliency value"""

    name: Literal["object/operator/saliency"] = field(default="object/operator/saliency")
    """Is always object/operator/saliency"""


@dataclass
class OperatorPupil(VectorData):
    """
        Information of the operator's eyes.
    Measurement unit: (complex)
    Value range: (unbounded)
    Recommended distribution: rectangular
    Elements of vector:
     - lp: (unit: mm) left pupil diameter
     - rp: (unit: mm) right pupil diameter
     - li: (unit: mm) left iris diameter
     - ri: (unit: mm) right iris diameter
     - lo: (unit: (dimensionless)) left openness range
     - ro: (unit: (dimensionless)) right openness range
     - fs: (unit: (dimensionless)) focus stability range
    """

    val: tuple[Number, Number, Number, Number, Number, Number, Number] = field(
        default_factory=lambda: no_default(field="OperatorPupil.val"), metadata=required
    )
    """Operator pupil value"""

    name: Literal["object/operator/pupil"] = field(default="object/operator/pupil")
    """Is always object/operator/pupil"""


@dataclass
class OperatorHandInteractionArea(VectorData):
    """
        Tuple of the left and right hand interaction area.
    Measurement unit: (dimensionless)
    Value range: (enumeration)
    Recommended distribution: probability vector
    Possible values:
     - STEERING_WHEEL: Hand is on steering wheel
     - CENTER_DISPLAY: Hand is on center display
     - ARMREST: Hand is on armrest
     - OTHER: Hand is on other element
    """

    val: tuple[str, str] = field(default_factory=lambda: no_default(field="OperatorHandInteractionArea.val"), metadata=required)
    """Operator hand_interaction_area value"""

    name: Literal["object/operator/hand_interaction_area"] = field(default="object/operator/hand_interaction_area")
    """Is always object/operator/hand_interaction_area"""


@dataclass
class OperatorSixDofRotationAndAcceleration(VectorData):
    """
        For driving simulator studies: Current parameters to a six-degrees-of-freedom physical driving simulator, if used.
    This can be used to evaluate the settings of a suitable physical driving simulator (e.g., a hexapod), which is the seat of the driving simulator and can exert forces onto the participant. For physical limitations, these values may differ from the actual physical properties of the simulated vehicle.
    Measurement unit: (complex)
    Value range: (unbounded)
    Recommended distribution: rectangular
    Elements of vector:
     - x: (unit: m/s²) Acceleration in x direction
     - y: (unit: m/s²) Acceleration in y direction.
     - z: (unit: rad/s²) Acceleration in z direction.
     - rx: (unit: rad) Euler roll angle (positive: right roll).
     - ry: (unit: rad) Euler pitch angle (positive: pitch down).
     - rz: (unit: rad) Euler yaw angle (positive: yaw left).
    """

    val: tuple[Number, Number, Number, Number, Number, Number] = field(
        default_factory=lambda: no_default(field="OperatorSixDofRotationAndAcceleration.val"), metadata=required
    )
    """Operator six_dof_rotation_and_acceleration value"""

    name: Literal["object/operator/six_dof_rotation_and_acceleration"] = field(
        default="object/operator/six_dof_rotation_and_acceleration"
    )
    """Is always object/operator/six_dof_rotation_and_acceleration"""

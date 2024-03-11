# Copyright © 2024 understandAI GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files
# (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from uai_openlabel import (
    CoordinateSystem,
    CoordinateSystemUid,
    EventUid,
    FrameInterval,
    ObjectUid,
    Uid,
)

from aveas_openlabel import (
    AveasOpenLabel,
)
from aveas_openlabel.attributes.dimension import Dimensions__Size
from aveas_openlabel.attributes.general import (
    Acceleration,
    BoundingBox,
    IsRecorder,
    Velocity,
)
from aveas_openlabel.attributes.interior import (
    Interior__BrakePedal,
    Interior__SteeringAngle,
)
from aveas_openlabel.attributes.lights import (
    Lights__Brake,
    Lights__Daytime,
    Lights__Front,
    Lights__HighBeam,
    Lights__Indicator__Left,
    Lights__Indicator__Right,
)
from aveas_openlabel.attributes.open_drive import (
    OpenDrive__LocalRoadCoordinates,
    OpenDrive__RoadId,
)
from aveas_openlabel.attributes.road import (
    Road__Classification,
    Road__ClassificationValue,
    Road__NumberLanes__Left__Legal,
    Road__NumberLanes__Left__Physical,
    Road__NumberLanes__Right__Legal,
    Road__NumberLanes__Right__Physical,
    Road__SpeedLimit,
)
from aveas_openlabel.attributes.summary import (
    Summary__Accel__Max,
    Summary__Accel__Min,
    Summary__Coordinates__ScenarioEnd,
    Summary__Coordinates__ScenarioStart,
    Summary__Speed__Max,
    Summary__Speed__Min,
    Summary__SteeringWheelAngle__Max,
    Summary__SteeringWheelAngle__Min,
)
from aveas_openlabel.classifications.car import Car
from aveas_openlabel.classifications.truck import Truck
from aveas_openlabel.contexts.environment_context import (
    EnvironmentContext,
    EnvironmentContextData,
)
from aveas_openlabel.contexts.environment_context_data import (
    Environment__CloudCover,
    Environment__LightingConditions,
    Environment__LightingConditionsValue,
    Environment__PrecipitationIntensity,
    Environment__RoadCondition,
    Environment__RoadConditionValue,
    Environment__Temperature,
    Environment__VisibilityRange,
    Environment__Wind__BeaufortForce,
    Environment__Wind__Heading,
)
from aveas_openlabel.contexts.scenario_context import (
    ScenarioContext,
    ScenarioContextData,
)
from aveas_openlabel.contexts.scenario_context_data import (
    Scenario__ContainsHighway,
    Scenario__ContainsRural,
    Scenario__ContainsUrban,
    Scenario__Course,
    Scenario__End__Coordinates,
    Scenario__End__Location,
    Scenario__IsBiased,
    Scenario__IsSampled,
    Scenario__IsSampled__ReferenceToSourceScenario,
    Scenario__IsStaged,
    Scenario__MaximumVehicleSpeed,
    Scenario__MaximumVehicleSpeed__Frame,
    Scenario__MinimumVehicleDistanceS,
    Scenario__MinimumVehicleDistanceS__Frame,
    Scenario__MinimumVehicleSpeed,
    Scenario__MinimumVehicleSpeed__Frame,
    Scenario__RatioAverageSpeedToSpeedLimit,
    Scenario__Start__Coordinates,
    Scenario__Start__Location,
    Scenario__WeekdayNumber,
)
from aveas_openlabel.event import (
    Event,
    EventData,
    EventTypeValue,
    RoleAParticipantID,
    RoleBParticipantIDs,
)
from aveas_openlabel.metadata import AcquisitionMethod, Metadata, RightOfUse
from aveas_openlabel.object_data.unattached import ObjectData__Unattached
from aveas_openlabel.object_in_frame_data.no_rider import ObjectInFrameData__NoRider


def test_example() -> None:
    # Create metadata
    annotator = "Porsche Engineering Group GmbH"
    comment = "This is a skeleton OpenLABEL."
    file_version = "0"
    name = "Skeleton OpenLABEL"
    right_of_use = RightOfUse.RESEARCH_ONLY
    acquisition_method = AcquisitionMethod.IN_VEHICLE
    acquisition_partner = "PEG"
    acquisition_date = "yyyy-MM-ddTHH:mm:ss.FFFZ"
    metadata = Metadata(
        schema_version="1.0.0",
        annotator=annotator,
        comment=comment,
        file_version=file_version,
        name=name,
        right_of_use=right_of_use,
        acquisition_method=acquisition_method,
        acquisition_partner=acquisition_partner,
        acquisition_date=acquisition_date,
    )

    # Create contexts
    # - 0: `ScenarioContext`,
    # - 1: `EnvironmentContext`,

    # Set Scenario Context
    rural_scenario = Scenario__ContainsRural(False)
    urban_scenario = Scenario__ContainsUrban(False)
    highway_scenario = Scenario__ContainsHighway(True)
    sampled_scenario = Scenario__IsSampled(False)
    biased_scenario = Scenario__IsBiased(False)
    staged_scenario = Scenario__IsStaged(False)
    minimum_vehicle_velocity = Scenario__MinimumVehicleSpeed(0)
    maximum_vehicle_velocity = Scenario__MaximumVehicleSpeed(0)
    minimum_vehicle_distance_s = Scenario__MinimumVehicleDistanceS(0)
    weekday_number = Scenario__WeekdayNumber(0)
    ratio_average_speed_to_speed_limit = Scenario__RatioAverageSpeedToSpeedLimit(0)
    scenario_start_location = Scenario__Start__Location("")
    scenario_end_location = Scenario__End__Location("")
    reference_to_source_scenario = Scenario__IsSampled__ReferenceToSourceScenario("")
    frame_minimum_vehicle_velocity = Scenario__MinimumVehicleSpeed__Frame("")
    frame_maximum_vehicle_velocity = Scenario__MaximumVehicleSpeed__Frame("")
    frame_minimum_vehicle_distance_s = Scenario__MinimumVehicleDistanceS__Frame("")
    scenario_start_coordinates = Scenario__Start__Coordinates((0, 0, 0))
    scenario_end_coordinates = Scenario__End__Coordinates((0, 0, 0))
    scenario_course = Scenario__Course(["0", "0", "0"])

    scenario_context_data = ScenarioContextData(
        boolean=[rural_scenario, urban_scenario, highway_scenario, sampled_scenario, biased_scenario, staged_scenario],
        num=[
            minimum_vehicle_velocity,
            maximum_vehicle_velocity,
            minimum_vehicle_distance_s,
            weekday_number,
            ratio_average_speed_to_speed_limit,
        ],
        text=[
            scenario_start_location,
            scenario_end_location,
            reference_to_source_scenario,
            frame_minimum_vehicle_velocity,
            frame_maximum_vehicle_velocity,
            frame_minimum_vehicle_distance_s,
        ],
        vec=[scenario_start_coordinates, scenario_end_coordinates, scenario_course],
    )

    scenario_context = ScenarioContext(context_data=scenario_context_data)

    # Set Environment Context
    weather_temperature_celsius = Environment__Temperature(0)
    weather_wind_beaufort_force = Environment__Wind__BeaufortForce(0)
    weather_wind_heading = Environment__Wind__Heading(0)
    weather_cloud_cover = Environment__CloudCover(0)
    lighting_conditions = Environment__LightingConditions(Environment__LightingConditionsValue("day"))
    road_condition = Environment__RoadCondition(Environment__RoadConditionValue("dry"))
    weather_visibility_range = Environment__VisibilityRange(40)
    weather_precipitation_intensity = Environment__PrecipitationIntensity(0)

    environment_context_data = EnvironmentContextData(
        boolean=[],
        num=[
            weather_temperature_celsius,
            weather_wind_beaufort_force,
            weather_wind_heading,
            weather_visibility_range,
            weather_cloud_cover,
            weather_precipitation_intensity,
        ],
        text=[lighting_conditions, road_condition],
        vec=[],
    )

    environment_context = EnvironmentContext(context_data=environment_context_data)

    contexts = {Uid("0"): scenario_context, Uid("1"): environment_context}

    # Create Coordinate Systems
    cs_uid = CoordinateSystemUid("00000001")
    coordinate_system = CoordinateSystem(
        children=[CoordinateSystemUid("uid_c1"), CoordinateSystemUid("uid_c2")],
        parent=CoordinateSystemUid("uid_p"),
        type="sensor_cs",
    )

    # Create events
    event_uid = EventUid("00000001")
    role_a_participant_id = RoleAParticipantID(Uid("1"))
    role_b_participant_i_ds = RoleBParticipantIDs([Uid("2"), Uid("3")])
    event_data = EventData(boolean=[], num=[], text=[role_a_participant_id], vec=[role_b_participant_i_ds])
    name = "event0"
    frame_intervals = [FrameInterval(frame_start=Uid("0"), frame_end=Uid("1"))]
    event = Event(event_data=event_data, name=name, frame_intervals=frame_intervals, type=EventTypeValue.LANE_CHANGE)

    # sample car
    three_d_bounding_box_euler = BoundingBox((0, 0, 0, 0, 0, 0, 0, 0, 0))
    velocity = Velocity((0, 0, 0, 0, 0, 0))
    acceleration = Acceleration((0, 0, 0, 0, 0, 0))
    speed_limit_value = Road__SpeedLimit(50)
    road_classification = Road__Classification(Road__ClassificationValue.STRAIGHT)  # ("straight"))
    number_lanes_left_legal = Road__NumberLanes__Left__Legal(1)
    number_lanes_left_physical = Road__NumberLanes__Left__Physical(1)
    number_lanes_right_legal = Road__NumberLanes__Right__Legal(1)
    number_lanes_right_physical = Road__NumberLanes__Right__Physical(1)
    steering_angle = Interior__SteeringAngle(0)
    brake_lights = Lights__Brake(False)
    indicator_left = Lights__Indicator__Left(False)
    indicator_right = Lights__Indicator__Right(False)
    front_lights = Lights__Front(False)
    daytime_lights = Lights__Daytime(False)
    high_beam_lights = Lights__HighBeam(False)
    open_drive_road_id = OpenDrive__RoadId("1")
    open_drive_local_road_coordinates = OpenDrive__LocalRoadCoordinates((0, 0))
    brake_pressure = Interior__BrakePedal(0)

    ObjectInFrameData__NoRider(
        boolean=[brake_lights, indicator_left, indicator_right, front_lights, daytime_lights, high_beam_lights],
        cuboid=[three_d_bounding_box_euler],
        vec=[velocity, acceleration, open_drive_local_road_coordinates],
        num=[
            number_lanes_left_legal,
            number_lanes_left_physical,
            number_lanes_right_legal,
            number_lanes_right_physical,
            steering_angle,
            speed_limit_value,
            brake_pressure,
        ],
        text=[road_classification, open_drive_road_id],
        bbox=None,
        rbbox=None,
    )

    # sample truck
    three_d_bounding_box_euler = BoundingBox((0, 0, 0, 0, 0, 0, 0, 0, 0))
    velocity = Velocity((0, 0, 0, 0, 0, 0))
    acceleration = Acceleration((0, 0, 0, 0, 0, 0))
    speed_limit_value = Road__SpeedLimit(50)
    road_classification = Road__Classification(Road__ClassificationValue("straight"))
    number_lanes_left_legal = Road__NumberLanes__Left__Legal(1)
    number_lanes_left_physical = Road__NumberLanes__Left__Physical(1)
    number_lanes_right_legal = Road__NumberLanes__Right__Legal(1)
    number_lanes_right_physical = Road__NumberLanes__Right__Physical(1)
    open_drive_road_id = OpenDrive__RoadId("1")
    open_drive_local_road_coordinates = OpenDrive__LocalRoadCoordinates((0, 0))

    ObjectInFrameData__NoRider(
        boolean=[],
        num=[
            speed_limit_value,
            number_lanes_left_legal,
            number_lanes_left_physical,
            number_lanes_right_legal,
            number_lanes_right_physical,
        ],
        text=[open_drive_road_id, road_classification],
        vec=[velocity, acceleration, open_drive_local_road_coordinates],
        cuboid=[three_d_bounding_box_euler],
    )

    # Create objects
    # sample car
    is_recorder = IsRecorder(True)
    dimensions_size = Dimensions__Size((0, 0, 0))
    summary_speed_max = Summary__Speed__Max(0)
    summary_speed_min = Summary__Speed__Min(0)
    summary_accel_max = Summary__Accel__Max(0)
    summary_accel_min = Summary__Accel__Min(0)
    summary_steering_wheel_angle_max = Summary__SteeringWheelAngle__Max(0)
    summary_steering_wheel_angle_min = Summary__SteeringWheelAngle__Min(0)
    summary_start_coordinate = Summary__Coordinates__ScenarioStart((0, 0, 0))
    summary_end_coordinate = Summary__Coordinates__ScenarioEnd((0, 0, 0))

    car_object_data = ObjectData__Unattached(
        boolean=[is_recorder],
        num=[
            summary_speed_max,
            summary_speed_min,
            summary_accel_max,
            summary_accel_min,
            summary_steering_wheel_angle_max,
            summary_steering_wheel_angle_min,
        ],
        text=[],
        vec=[dimensions_size, summary_start_coordinate, summary_end_coordinate],
    )

    car = Car(name="Car01", type="vehicle/car", object_data=car_object_data)

    # sample truck
    is_recorder = IsRecorder(False)
    dimensions_size = Dimensions__Size((0, 0, 0))
    summary_speed_max = Summary__Speed__Max(0)
    summary_speed_min = Summary__Speed__Min(0)
    summary_accel_max = Summary__Accel__Max(0)
    summary_accel_min = Summary__Accel__Min(0)
    summary_start_coordinate = Summary__Coordinates__ScenarioStart((0, 0, 0))
    summary_end_coordinate = Summary__Coordinates__ScenarioEnd((0, 0, 0))

    truck_object_data = ObjectData__Unattached(
        boolean=[is_recorder],
        num=[summary_speed_max, summary_speed_min, summary_accel_max, summary_accel_min],
        text=[],
        vec=[dimensions_size, summary_start_coordinate, summary_end_coordinate],
    )

    truck = Truck(name="Truck01", type="vehicle/truck", object_data=truck_object_data)

    scenario_objects = {ObjectUid("00000001"): car, ObjectUid("00000001"): truck}

    # Create ontologies

    # Create resources

    aveas_openlabel_example = AveasOpenLabel(
        metadata=metadata,
        contexts=contexts,
        coordinate_systems={cs_uid: coordinate_system},
        events={event_uid: event},
        frame_intervals=None,
        frames=None,
        objects=scenario_objects,
        ontologies=None,
        resources=None,
    )
    # Code to populate aveas_openlabel_example
    aveas_openlabel_example.to_dict(exclude_none=True, exclude_defaults=False)

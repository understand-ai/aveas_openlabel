"""AVEAS OpenLABEL library root

===============
AVEAS OpenLABEL
===============

Welcome to the documentation for the AVEAS OpenLABEL implementation in Python.
This library supports you in reading and writing AVEAS OpenLABEL JSON files by providing a nested dataclass structure that reflects the JSON schema.

AVEAS OpenLABEL is a subset of the base ASAM OpenLABEL specification.
This means that AVEAS OpenLABEL files are always valid ASAM OpenLABEL files.

The core class of this repository is `AveasOpenLabel`, which represents the root of the AVEAS OpenLabel JSON.

Reading AVEAS OpenLABEL files
-----------------------------

Parsing an existing AVEAS OpenLABEL JSON file can be done with

>>> import json
>>> from aveas_openlabel import AveasOpenLabel
>>> with open("path/to/input.json", "r") as f:
...     content = json.load(f)
>>> aveas_openlabel_example = AveasOpenLabel.from_dict(content)

Writing AVEAS OpenLABEL files
-----------------------------

Writing a populated OpenLABEL dataclass structure to a JSON file is similarly simple

>>> import json
>>> from aveas_openlabel import AveasOpenLabel
>>> aveas_openlabel_example = AveasOpenLabel.minimum_example()
>>> content = aveas_openlabel_example.to_dict()
>>> with open("path/to/file.json", "w") as f:
...     json.dump(content, f)

Obtaining a JSON schema file
----------------------------

A JSON schema file can be extracted from the root AveasOpenLabel class.

>>> import json
>>> from apischema.json_schema import serialization_schema
>>> from aveas_openlabel import AveasOpenLabel
>>> schema = serialization_schema(AveasOpenLabel)
>>> with open("path/to/file.json", "w") as f:
...     json.dump(schema, f)


Classifications and attributes
------------------------------

* A list of classifications can be found under `aveas_openlabel.classifications`.
* The static attributes of an object are written into the `AveasOpenLabel.objects` field.
* Dynamic attributes of an object are written into the `Frame.objects` field of each `Frame` object inside
  `AveasOpenLabel.frames`.

AVEAS OpenLABEL has mandatory and optional attributes defined for each classification.
The following tables indicate optional ("**O**") and mandatory ("**M**") attributes for each classification.
A "**—**" means that the attribute is not defined for the classification.

Static Attributes
`````````````````

.. table:: Static attributes per classification
    :widths: grid

    ==============================================  ========  =========  =====  =====  =================  ================  ============  =============  ==================  =============  =========  =======  =====
    Static attributes                               Object entries in `AveasOpenLabel.objects`
    ----------------------------------------------  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    **.**                                           `Animal`  `Bicycle`  `Bus`  `Car`  `HumanPedestrian`  `MobilityDevice`  `Motorcycle`  `OtherObject`  `PushablePullable`  `RailVehicle`  `Trailer`  `Truck`  `Van`
    ==============================================  ========  =========  =====  =====  =================  ================  ============  =============  ==================  =============  =========  =======  =====
    `IsRecorder`                                    **—**     **M**      **M**  **M**  **M**              **M**             **M**         **M**          **—**               **M**          **—**      **M**    **M**
    `AttachedTo`                                    **—**     **—**      **—**  **—**  **—**              **—**             **—**         **O**          **O**               **O**          **O**      **—**    **—**
    `Impact__Point`                                 **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Impact__Point__UStdDev`                        **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Impact__Velocity`                              **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Impact__Velocity__UStdDev`                     **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Impact__Frame`                                 **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Classification__Uncertainties`                 **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Dimensions__Size`                              **M**     **M**      **M**  **M**  **M**              **M**             **M**         **M**          **M**               **M**          **M**      **M**    **M**
    `Dimensions__Size__UStdDev`                     **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Dimensions__CenterOfGravity`                   **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Dimensions__CenterOfGravity__UStdDev`          **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Speed__Max`                           **M**     **M**      **M**  **M**  **M**              **M**             **M**         **M**          **M**               **M**          **M**      **M**    **M**
    `Summary__Speed__Max__UStdDev`                  **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Speed__Min`                           **M**     **M**      **M**  **M**  **M**              **M**             **M**         **M**          **M**               **M**          **M**      **M**    **M**
    `Summary__Speed__Min__UStdDev`                  **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Accel__Max`                           **M**     **M**      **M**  **M**  **M**              **M**             **M**         **M**          **M**               **M**          **M**      **M**    **M**
    `Summary__Accel__Max__UStdDev`                  **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Accel__Min`                           **M**     **M**      **M**  **M**  **M**              **M**             **M**         **M**          **M**               **M**          **M**      **M**    **M**
    `Summary__Accel__Min__UStdDev`                  **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__SteeringWheelAngle__Max`              **—**     **O**      **O**  **O**  **—**              **O**             **O**         **O**          **—**               **—**          **—**      **O**    **O**
    `Summary__SteeringWheelAngle__Max__UStdDev`     **—**     **O**      **O**  **O**  **—**              **O**             **O**         **O**          **—**               **—**          **—**      **O**    **O**
    `Summary__SteeringWheelAngle__Min`              **—**     **O**      **O**  **O**  **—**              **O**             **O**         **O**          **—**               **—**          **—**      **O**    **O**
    `Summary__SteeringWheelAngle__Min__UStdDev`     **—**     **O**      **O**  **O**  **—**              **O**             **O**         **O**          **—**               **—**          **—**      **O**    **O**
    `Summary__SteeringAngle__Max`                   **—**     **M**      **M**  **M**  **—**              **M**             **M**         **M**          **—**               **—**          **—**      **M**    **M**
    `Summary__SteeringAngle__Max__UStdDev`          **—**     **O**      **O**  **O**  **—**              **O**             **O**         **O**          **—**               **—**          **—**      **O**    **O**
    `Summary__SteeringAngle__Min`                   **—**     **M**      **M**  **M**  **—**              **M**             **M**         **M**          **—**               **—**          **—**      **M**    **M**
    `Summary__SteeringAngle__Min__UStdDev`          **—**     **O**      **O**  **O**  **—**              **O**             **O**         **O**          **—**               **—**          **—**      **O**    **O**
    `Summary__Coordinates__ScenarioStart`           **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Coordinates__ScenarioStart__UStdDev`  **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Coordinates__ScenarioEnd`             **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Summary__Coordinates__ScenarioEnd__UStdDev`    **O**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **O**               **O**          **O**      **O**    **O**
    `Operator__Age`                                 **—**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **—**               **O**          **—**      **O**    **O**
    `Operator__Gender`                              **—**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **—**               **O**          **—**      **O**    **O**
    `Operator__Personality`                         **—**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **—**               **O**          **—**      **O**    **O**
    `Operator__BodyHeight`                          **—**     **O**      **O**  **O**  **O**              **O**             **O**         **O**          **—**               **O**          **—**      **O**    **O**
    ==============================================  ========  =========  =====  =====  =================  ================  ============  =============  ==================  =============  =========  =======  =====

Dynamic Attributes
``````````````````

.. table:: Dynamic attributes per classification
    :widths: grid

    ==============================================  ===============  ================  ============  ============  ========================  =======================  ===================  ====================  =========================  ====================  ================  ==============  ============
    Dynamic attributes                              Object entries in `Frame.objects` inside `AveasOpenLabel.frames`
    ----------------------------------------------  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    **.**                                           `AnimalInFrame`  `BicycleInFrame`  `BusInFrame`  `CarInFrame`  `HumanPedestrianInFrame`  `MobilityDeviceInFrame`  `MotorcycleInFrame`  `OtherObjectInFrame`  `PushablePullableInFrame`  `RailVehicleInFrame`  `TrailerInFrame`  `TruckInFrame`  `VanInFrame`
    ==============================================  ===============  ================  ============  ============  ========================  =======================  ===================  ====================  =========================  ====================  ================  ==============  ============
    `BoundingBox`                                   **M**            **M**             **M**         **M**         **M**                     **M**                    **M**                **M**                 **M**                      **M**                 **M**             **M**           **M**
    `BoundingBox__UStdDev`                          **O**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **O**                      **O**                 **O**             **O**           **O**
    `Velocity`                                      **M**            **M**             **M**         **M**         **M**                     **M**                    **M**                **M**                 **M**                      **M**                 **M**             **M**           **M**
    `Velocity__UStdDev`                             **O**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **O**                      **O**                 **O**             **O**           **O**
    `Acceleration`                                  **M**            **M**             **M**         **M**         **M**                     **M**                    **M**                **M**                 **M**                      **M**                 **M**             **M**           **M**
    `Acceleration__UStdDev`                         **O**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **O**                      **O**                 **O**             **O**           **O**
    `Interior__HasRider`                            **—**            **M**             **—**         **—**         **—**                     **M**                    **M**                **M**                 **—**                      **—**                 **—**             **—**           **—**
    `Interior__SteeringAngle`                       **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **—**                 **—**             **O**           **O**
    `Interior__SteeringAngle__UStdDev`              **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **—**                 **—**             **O**           **O**
    `Interior__AutomatedControl__Longitudinal`      **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Interior__AutomatedControl__Lateral`           **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **—**                 **—**             **O**           **O**
    `Interior__Wiper`                               **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Interior__Gear`                                **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Interior__AcceleratorPedal`                    **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Interior__BrakePedal`                          **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Lights__Brake`                                 **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **O**             **O**           **O**
    `Lights__Indicator__Left`                       **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **O**             **O**           **O**
    `Lights__Indicator__Right`                      **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **O**             **O**           **O**
    `Lights__Front`                                 **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **O**             **O**           **O**
    `Lights__Daytime`                               **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **O**             **O**           **O**
    `Lights__HighBeam`                              **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **O**             **O**           **O**
    `OpenDrive__RoadId`                             **O**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **O**                      **O**                 **O**             **O**           **O**
    `OpenDrive__LocalRoadCoordinates`               **M**            **M**             **M**         **M**         **M**                     **M**                    **M**                **M**                 **M**                      **M**                 **M**             **M**           **M**
    `OpenDrive__LocalRoadCoordinates__UStdDev`      **O**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **O**                      **O**                 **O**             **O**           **O**
    `Traffic__Density`                              **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Traffic__Density__UStdDev`                     **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Traffic__Volume`                               **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Traffic__Volume__UStdDev`                      **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Road__SpeedLimit`                              **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Road__Classification`                          **—**            **M**             **M**         **M**         **—**                     **M**                    **M**                **M**                 **—**                      **M**                 **M**             **M**           **M**
    `Road__NumberLanes__Left__Legal`                **—**            **M**             **M**         **M**         **—**                     **M**                    **M**                **M**                 **—**                      **M**                 **M**             **M**           **M**
    `Road__NumberLanes__Left__Physical`             **—**            **M**             **M**         **M**         **—**                     **M**                    **M**                **M**                 **—**                      **M**                 **M**             **M**           **M**
    `Road__NumberLanes__Right__Legal`               **—**            **M**             **M**         **M**         **—**                     **M**                    **M**                **M**                 **—**                      **M**                 **M**             **M**           **M**
    `Road__NumberLanes__Right__Physical`            **—**            **M**             **M**         **M**         **—**                     **M**                    **M**                **M**                 **—**                      **M**                 **M**             **M**           **M**
    `Operator__HeadRotation`                        **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__HeadRotation__UStdDev`               **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__FocussedPoint`                       **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__FocussedPoint__UStdDev`              **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__ViewingAngle`                        **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__FocussedObject`                      **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__FocussedObject__Uncertainties`       **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__FocussedObject__Id`                  **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__Pupil`                               **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__Pupil__UStdDev`                      **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__HandInteractionArea`                 **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `Operator__SixDoFRotationAndAcceleration`       **—**            **O**             **O**         **O**         **O**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `HmiFeedback__Visual`                           **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `HmiFeedback__Acoustic`                         **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    `HmiFeedback__Other`                            **—**            **O**             **O**         **O**         **—**                     **O**                    **O**                **O**                 **—**                      **O**                 **—**             **O**           **O**
    ==============================================  ===============  ================  ============  ============  ========================  =======================  ===================  ====================  =========================  ====================  ================  ==============  ============

"""

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


# noinspection PyProtectedMember
from aveas_openlabel.aveas_openlabel import AveasOpenLabel

__all__ = [
    "AveasOpenLabel",
]

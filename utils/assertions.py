from jsonschema import validate
from pydantic import BaseModel


class Assert:
    @staticmethod
    def validate_schema(instance: dict) -> None:
        validate(instance=instance, schema=BaseModel.schema())

    schema = {
        "type": "object", #type, properties a
        "properties": {
            "name": {"type": "string"},
            "job": {"type": "string"
                    },
            "id": {"type": "string"},
            "createdId": {
                "type": "string"
            }
        }
    }
    message = {"name": "Morpheus", "age": 35, "role": "user"}

    def validate_schema_custom(self) -> None:
        validate(instance=self.message, schema=self.schema)

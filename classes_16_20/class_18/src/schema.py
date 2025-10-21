from pydantic import BaseModel


# this class is the view, schema or data contract
class PokemonSchema(BaseModel):
    name: str
    type: str

    model_config = {"from_attributes": True}

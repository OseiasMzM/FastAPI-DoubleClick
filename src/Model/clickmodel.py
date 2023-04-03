from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class Cliques(BaseModel):
    id: Optional[int] = None
    primeiro_clique: datetime
    segundo_clique: datetime
    diferenca: Optional[float]
from dataclasses import dataclass, field

@dataclass
class Poll:
    title: str
    options: list = field(default_factory=list)

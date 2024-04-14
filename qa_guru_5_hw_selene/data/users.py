import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birth_day: str
    birth_month: str
    birth_year: str
    subjects: str
    hobbies: str
    picture_path: str
    address: str
    state: str
    city: str

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def state_and_city(self):
        return f'{self.state} {self.city}'

    def date_of_birth(self):
        return f'{self.birth_day} {self.birth_month},{self.birth_year}'

    def short_subject(self) -> str:
        return self.subjects[:2]

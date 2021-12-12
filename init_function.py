class car:

    def __init__(self, pilot, model, color, company):
        self.pilot = pilot
        self.model = model
        self.color = color
        self.company = company 

type = car('Ayrton Senna','MP4/4', 'white and red', 'McLaren')
print(f'The pilot of the {type.color} {type.model} by the {type.company} company is {type.pilot}.')
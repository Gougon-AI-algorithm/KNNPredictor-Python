class Factor():
    def __init__(self, wind, power, pitch):
        self.wind = float(wind)
        self.power = float(power)
        self.pitch = float(pitch)
        
    def get_wind(self):
        return self.wind
    
    def set_wind(self, wind):
        self.wind = wind
        
    def get_power(self):
        return self.power
    
    def set_power(self, power):
        self.power = power
        
    def get_pitch(self):
        return self.pitch
    
    def set_pitch(self, pitch):
        self.pitch = pitch
        
    def get_euclidean(self, another):
        wind = abs(self.wind - another.get_wind())
        power = abs(self.power - another.get_power())
        return pow(wind, 2) + pow(power, 2)
MACHINE_ATTR_NAME = 'Wind_turbine_name'

class DFHelper():
    def set_dataframe(self, dataframe):
        self.dataframe = dataframe
        
    def get_dataframe(self):
        return self.dataframe
    
    def choose_needed_data(self, names, attrs):
        self._clear_noneed_name(names)
        self._clear_noneed_attr(attrs)
        
    def _clear_noneed_name(self, names):
        name_mask = self.dataframe[MACHINE_ATTR_NAME].isin(names)
        self.dataframe = self.dataframe[name_mask]
        
    def _clear_noneed_attr(self, attrs):
        self.dataframe = self.dataframe[attrs]
        
    def drop_na(self):
        self.dataframe.dropna()
        
    def transform_df_to_float(self):
        self.dataframe['Ws'] = self.dataframe['Ws'].astype(float)
        self.dataframe['Ba'] = self.dataframe['Ba'].astype(float)
        self.dataframe['P'] = self.dataframe['P'].astype(float)
        
    def head(self):
        print(self.dataframe.head())
        
    def get_column(self, name):
        return self.dataframe[name]
        
    
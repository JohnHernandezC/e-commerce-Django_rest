
from django.db import models
from Apps.base. models import BaseModel
from simple_history.models import HistoricalRecords 

   

class MeasureUnit (BaseModel):
    
    description = models.CharField(max_length=50, blank=True, null=False, unique=True)
    historical= HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    class Meta:
        
       
        verbose_name = "unidad de medida"
        verbose_name_plural ="unidades de medida"
    def __str__(self):
        return self.description    
    
class CategoryProduct (BaseModel):
    
    description = models.CharField(max_length=50, blank=True, null=False, unique=True)
    
    historical= HistoricalRecords()
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    class Meta:
        
       
        verbose_name = "categoria producto"
        verbose_name_plural ="categorias productos"
    def __str__(self):
        return self.description   

class Indicator (BaseModel):
    descountValue= models.PositiveIntegerField(default=0)
    categoryProduct = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    historical= HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value

    class Meta:
        verbose_name = 'indicador de oferta'
        verbose_name_plural = 'indicadores de ofertas'

    def __str__(self):
        return f'oferta dela categoria {self.categoryProduct} : {self.descountValue}'
        
class Product(BaseModel):
    
    name = models.CharField(max_length=150, blank=False, unique=True, null=False)
    description= models.TextField(blank=False, unique=True, null=False)
    image = models.CharField( blank=True, null=True,  max_length=1000)
    MeasureUnit= models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, null=True )
    categoryProduc= models.ForeignKey(CategoryProduct, on_delete=models.CASCADE, null=True )    
    historical= HistoricalRecords()
    
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value


    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

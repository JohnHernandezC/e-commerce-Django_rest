# Generated by Django 4.0.4 on 2022-06-29 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoryproduct',
            name='MeasureUnit',
        ),
        migrations.RemoveField(
            model_name='historicalcategoryproduct',
            name='MeasureUnit',
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='MeasureUnit',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.measureunit'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='categoryProduc',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='products.categoryproduct'),
        ),
        migrations.AddField(
            model_name='product',
            name='MeasureUnit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.measureunit'),
        ),
        migrations.AddField(
            model_name='product',
            name='categoryProduc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='products.categoryproduct'),
        ),
    ]

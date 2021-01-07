# Generated by Django 3.1.3 on 2021-01-07 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20201231_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Basket',
                'verbose_name_plural': 'Baskets',
            },
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Count')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'BasketItem',
                'verbose_name_plural': 'BasketItems',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
                ('discription', models.TextField(verbose_name='Discription')),
                ('paid', models.BooleanField(default=False, verbose_name='Paid')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(verbose_name='Counts')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'OrderItem',
                'verbose_name_plural': 'OrderItems',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Paid Price')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Create At')),
                ('update_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('discription', models.TextField(verbose_name='Discription')),
                ('image', models.ImageField(upload_to='shop/shops', verbose_name='Image')),
                ('joined', models.DateTimeField(auto_now_add=True, verbose_name='Joined')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('closed', models.BooleanField(default=True, verbose_name='Closed')),
            ],
            options={
                'verbose_name': 'Shop',
                'verbose_name_plural': 'Shops',
            },
        ),
        migrations.CreateModel(
            name='ShopProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_products', related_query_name='shop_products', to='products.product', verbose_name='Product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_products', related_query_name='shop_products', to='shop.shop', verbose_name='Shop')),
            ],
            options={
                'verbose_name': 'ShopProduct',
                'verbose_name_plural': 'ShopProducts',
            },
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_product',
            field=models.ManyToManyField(related_name='shops', through='shop.ShopProduct', to='products.Product', verbose_name='Shop Product'),
        ),
    ]

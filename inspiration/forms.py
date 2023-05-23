from django import forms

def InputForm(forms.Form):
    title = models.CharField(max_length=150, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pc_builds')
    feature_image = CloudinaryField('image', default='placeholder')
    secondary_image = CloudinaryField('image', default='placeholder')
    tertiary_image = CloudinaryField('image', default='placeholder')
    created_on = models.DateTimeField(auto_now_add=True)
    cpu_content = models.CharField(max_length=150, default='CPU')
    cpu_cooler_content = models.CharField(max_length=150, default='CPU-Cooler')
    motherboard_content = models.CharField(max_length=150, default='Motherboard')
    ram_content = models.CharField(max_length=200, default='RAM')
    storage_content = models.CharField(max_length=250, default='Storage')
    gpu_content = models.CharField(max_length=150,  default='GPU')
    psu_content = models.CharField(max_length=150, default='PSU')
    case_content = models.CharField(max_length=150, default='Case')
    fans_content = models.CharField(max_length=150, default='Fans')
    
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post
from .forms import PostForm


class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            cpu='i7 8700k',
            cpu_manufacturer='Intel',
            cpu_cooler='Cooler Master',
            motherboard='ASUS ROG Strix ',
            ram='16GB',
            storage='500GB SSD',
            gpu='MSI Gaming X RTX 3080',
            gpu_manufacturer='Nvidia',
            psu='Corsair RM1000X',
            case='NZXT H10',
            fans='Noctua NF-12',
        )

    def test_post_model(self):
        self.assertEqual(str(self.post), 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.cpu, 'i7 8700k')
        self.assertEqual(self.post.cpu_manufacturer, 'Intel')
        self.assertEqual(self.post.cpu_cooler, 'Cooler Master')
        self.assertEqual(self.post.motherboard, 'ASUS ROG Strix')
        self.assertEqual(self.post.ram, '16GB')
        self.assertEqual(self.post.storage, '500GB SSD')
        self.assertEqual(self.post.gpu, 'MSI Gaming X RTX 3080')
        self.assertEqual(self.post.gpu_manufacturer, 'Nvidia')
        self.assertEqual(self.post.psu, 'Corsair RM1000X')
        self.assertEqual(self.post.case, 'Corsair 4000d')
        self.assertEqual(self.post.fans, 'Noctua NF-12')

    def test_post_form_valid(self):
        form_data = {
            'title': 'New Post',
            'cpu': 'Ryzen 7 5700x',
            'cpu_manufacturer': 'AMD',
            'cpu_cooler': 'NZXT Z73',
            'motherboard': 'Asus TUF Gaming X570-Plus',
            'ram': 'Corsair Vengance LPX 32gb',
            'storage': 'x2 2TB SSD',
            'gpu': 'Asus TUF Gaming OC RTX 3080',
            'gpu_manufacturer': 'Nvidia',
            'psu': 'Fractal Design Ion+ 860w',
            'case': 'Corsair 5000d',
            'fans': 'NZXT F120 RGB',
        }
        form = PostForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_post_form_invalid(self):
        form_data = {
            'title': 'Invalid',
            'cpu': 'Ryzen 3 3400g',
            'cpu_manufacturer': 'AMD',
            'cpu_cooler': '',
            'motherboard': 'AsRock B450',
            'ram': 'gSkill Trident Z Royal 8gb',
            'storage': '8TB HDD',
            'gpu': '',
            'gpu_manufacturer': '',
            'psu': 'Gigabyte 650w',
            'case': 'Lian Li o11 mini',
            'fans': 'Generic 120mm',
        }
        form = PostForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

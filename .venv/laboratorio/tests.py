from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio


class LaboratorioTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio de Prueba",
            ciudad="Santiago",
            pais="Chile"
        )

    def test_laboratorio_data(self):
        laboratorio = self.laboratorio
        self.assertEqual(laboratorio.nombre, "Laboratorio de Prueba")
        self.assertEqual(laboratorio.ciudad, "Santiago")
        self.assertEqual(laboratorio.pais, "Chile")

    def test_laboratorio_url(self):
        url = reverse('laboratorio:laboratorio_detail', args=[self.laboratorio.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_laboratorio_template(self):
        url = reverse('laboratorio:laboratorio_detail', args=[self.laboratorio.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'laboratorio/laboratorio_detail.html')

    def test_laboratorio_html_content(self):
        url = reverse('laboratorio:laboratorio_detail', args=[self.laboratorio.pk])
        response = self.client.get(url)
        self.assertContains(response, "Laboratorio de Prueba")
        self.assertContains(response, "Santiago")
        self.assertContains(response, "Chile")

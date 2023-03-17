# Tests

## Inspirational

* [`boosts/tests/test_inspirational_model.py`](../boosts/tests/test_inspirational_model.py):

    ```python
    def test_get_absolute_url(self):
        """
        `get_absolute_url` method should return a string in the format:
        `/boosts/inspirational/<id>/`
        """
        inspirational = Inspirational.objects.get(id=1)
        expected_url = f'/boosts/inspirational/{inspirational.id}/'
        self.assertEqual(inspirational.get_absolute_url(), expected_url)
    ```

* [`boosts/models.py`](../boosts/models.py):

    ```python
    class Inspirational(models.Model):
        # ...
        def get_absolute_url(self):
            return reverse("boosts:inspirational-detail", kwargs={"pk": self.pk})
    ```

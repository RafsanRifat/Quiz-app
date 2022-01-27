from django.db import models


# Create your models here.
class Quiz(models.Model):
    DEF_CHOICE = (
        ('easy', 'easy'),
        ('medium', 'medium'),
        ('hard', 'hard'),
    )
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes:")
    required_score_to_pass = models.IntegerField(help_text="required score : ")
    difficulty = models.CharField(max_length=6, choices=DEF_CHOICE)

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_question(self):
        return self.question_set.all()[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Quizes'

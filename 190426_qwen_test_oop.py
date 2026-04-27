print('🖥️ ФИНАЛЬНОЕ ЗАДАНИЕ: «Система сборки и тестирования ПК»')

# ================= КАРКАС ПРОЕКТА =================

class Builder:
    def __init__(self, name, surname, specialty):
        self.name = name
        self.surname = surname
        self.specialty = specialty
        self.completed_tasks = []
        self.tasks_in_progress = []
        self.build_scores = {}  # {'assembly': [9, 10], 'cabling': [8]}

    def _calc_avg(self):
        # Соберите все оценки из self.build_scores.values(), посчитайте среднее.
        # Если пусто → 0.0
        all_scores = [score for grades in self.build_scores.values() for score in grades]
        # "Распаковываем" вложенные списки в один плоский список всех оценок
        return sum(all_scores) / len(all_scores) if all_scores else 0.0
        # Защищаемся от деления на ноль и считаем среднее

    def rate_component(self, component, task, score):
        # 1. isinstance(component, Component)
        # 2. task в self.tasks_in_progress И в component.compatible_tasks
        # 3. 1 <= score <= 10 (используйте @staticmethod Component.validate_score(score))
        # Если ок → component.performance_ratings.setdefault(task, []).append(score), return None
        # Иначе → return 'Ошибка'
        if (isinstance(component, Component) and task in self.tasks_in_progress and task in component.compatible_tasks and Component.validate_score(score)):            
            component.performance_ratings.setdefault(task, []).append(score)
            return None
        return 'Ошибка'

    def __str__(self): ...
    def __repr__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __ne__(self, other): ...


class Hardware:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.certified_tasks = []

    def __str__(self): ...
    def __repr__(self): ...


class Component(Hardware):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.performance_ratings = {}  # {'stress_test': [9, 10]}

    @staticmethod
    def validate_score(score):
        return isinstance(score, (int, float)) and 1 <= score <= 10

    def _calc_avg(self):
        # Аналогично Builder._calc_avg(), но для self.performance_ratings
        ...

    def __str__(self): ...
    def __repr__(self): ...
    def __eq__(self, other): ...
    def __lt__(self, other): ...
    def __le__(self, other): ...
    def __gt__(self, other): ...
    def __ge__(self, other): ...
    def __ne__(self, other): ...


class QA_Engineer(Hardware):
    def __init__(self, brand, model):  # brand/model условны для инженера (например, отдел)
        super().__init__(brand, model)

    def rate_builder(self, builder, task, score):
        # 1. isinstance(builder, Builder)
        # 2. task в self.certified_tasks И в builder.tasks_in_progress
        # Если ок → builder.build_scores.setdefault(task, []).append(score)
        # Иначе → return 'Ошибка'
        ...


# ================= ВНЕШНИЕ ФУНКЦИИ АГРЕГАЦИИ =================
def avg_builder_scores(builders_list, task_name):
    # Соберите все оценки по task_name из builder.build_scores у всех сборщиков.
    # Верните sum/len или 0.0
    ...

def avg_component_scores(components_list, task_name):
    # То же самое, но для component.performance_ratings
    ...
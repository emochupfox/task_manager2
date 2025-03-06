# task_manager2

PROJECT NAME: task_manager
APPLICATION NAME: tasks

#CREATION OF TASK MODELS:
    def save(self, *args, **kwargs):
        if self.due_date and self.due_date < now().date():
            self.status = 'Overdue'
        elif self.status != 'Completed':
            self.status = 'Pending'
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

==============================
APPLYING OF MIGRATIONS AFTER::
==============================
THE HTML'S (FILES) [THE FOLLOWING]:

[task_confirm_delete]
<body>
    <div class="container mt-5">
        <div class="card shadow p-4 text-center" style="background-color: #F7A8C4;">
            <h2 class="text-danger">⚠ Are you sure?</h2>
            <p>You are about to delete "<strong>{{ task.title }}</strong>". This action cannot be undone.</p>
            <form method="POST">
                {% csrf_token %}
                <button type="submit" class="btn btn-danger btn-lg">🗑 Delete</button>
                <a href="{% url 'task_list' %}" class="btn btn-red btn-lg">↩ Cancel</a>
            </form>
        </div>
    </div>
</body>
 </body>
 </html>

[task_form]
            <div class="mb-3">
                <label for="id_title" class="form-label" style="color: black;">Title:</label>
                <input type="text" id="id_title" name="title" class="form-control text-center" placeholder="Enter Task Title" value="{{ form.title.value|default:'' }}">
            </div>
            <div class="mb-3">
                <label for="id_description" class="form-label" style="color: black;">Description:</label>
                <textarea id="id_description" name="description" class="form-control text-center" placeholder="Enter Task Description">{{ form.description.value|default:'' }}</textarea>
            </div>
            <div class="mb-3">
                <label for="id_due_date" class="form-label" style="color: black;">Due Date:</label>
                <input type="date" id="id_due_date" name="due_date" class="form-control text-center" value="{{ form.due_date.value|default:'' }}">
            </div>
            {% if form.instance.pk %} <!-- Only display for updates -->
            <div class="mb-3">
                <label for="id_status" class="form-label" style="color: black;">Status:</label>
                <select id="id_status" name="status" class="form-select text-center">
                    {% for choice in form.status.field.choices %}
                        <option value="{{ choice.0 }}" {% if choice.0 == form.status.value %}selected{% endif %}>
                            {{ choice.1 }}
                        </option>
                    {% endfor %}
                </select>
            </div>
</body>
[task_list]
 <table class="table table-striped table-dark text-center align-middle table-bordered">
            <thead class="thead-dark" style="background-color: rgb(71, 2, 5); color: white;">
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Due Date</th>
                    <th>Status</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>

 Define URLs ( urls.py ) 
 urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.task_create, name=////'task_create'),
    path('<int:id>/edit/', views.task_update, name='task_update'),
    path('<int:id>/delete/', views.task_delete, name='task_delete'),
///

-  task_list.html : Display all tasks.
   ![image](https://github.com/user-attachments/assets/5a515606-583b-49da-b551-8cc9a1a852d7)
 -  task_form.html : Form for creating/editing tasks.
   ![Screenshot 2025-03-06 213222](https://github.com/user-attachments/assets/15010979-6e8e-43a3-9e7b-1f1af6965ab1)
 -  task_confirm_delete.html : Confirmation before deleting a task.
     ![image](https://github.com/user-attachments/assets/ca5ab9c2-2a02-4312-a8f7-bafc798f3282)
 -  boostrap used:
     (https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css)

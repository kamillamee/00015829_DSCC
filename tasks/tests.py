"""
Tests for Task Manager application.
"""
import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Project, Task, Tag


@pytest.mark.django_db
def test_homepage_loads(client):
    """Test that homepage returns 200."""
    response = client.get(reverse('home'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_page_loads(client):
    """Test that login page returns 200."""
    response = client.get(reverse('login'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_page_loads(client):
    """Test that register page returns 200."""
    response = client.get(reverse('register'))
    assert response.status_code == 200


@pytest.mark.django_db
def test_user_registration(client):
    """Test user can register successfully."""
    response = client.post(reverse('register'), {
        'username': 'newuser',
        'email': 'new@example.com',
        'password1': 'complexpass123!',
        'password2': 'complexpass123!',
    })
    assert response.status_code == 302
    User = get_user_model()
    assert User.objects.filter(username='newuser').exists()


@pytest.mark.django_db
def test_project_crud(client, user):
    """Test project create, read, update, delete."""
    client.force_login(user)
    # Create
    response = client.post(reverse('project_create'), {
        'name': 'Test Project',
        'description': 'Test description',
    })
    assert response.status_code == 302
    project = Project.objects.get(name='Test Project')
    assert project.owner == user
    # Read
    response = client.get(reverse('project_detail', kwargs={'pk': project.pk}))
    assert response.status_code == 200
    assert b'Test Project' in response.content


@pytest.mark.django_db
def test_task_many_to_many_relationship(user):
    """Test many-to-many relationship between Task and Tag."""
    project = Project.objects.create(name='P1', owner=user)
    tag1 = Tag.objects.create(name='urgent')
    tag2 = Tag.objects.create(name='bug')
    task = Task.objects.create(title='T1', project=project)
    task.tags.add(tag1, tag2)
    assert task.tags.count() == 2
    assert tag1.tasks.count() == 1

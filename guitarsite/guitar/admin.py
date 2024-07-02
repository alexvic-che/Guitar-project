from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Sings, Difficulty, Authors


@admin.register(Sings)
class SingsAdmin(admin.ModelAdmin):
    list_display = ["title","time_create", "card_imagess" ,"is_published","difficult","author", "chords_info"]
    list_display_links = ["title"]
    list_editable = ["is_published", "difficult" ,"author"]
    list_per_page = 10
    readonly_fields = ["card_imagess"]
    ordering = ["-time_create"]
    actions = ["set_published", "set_draft"]
    search_fields = ["title", "author__name"]
    list_filter = ["is_published", "difficult", "author"]
    fields = ["title","slug","content","card_image", "card_imagess" ,"author","difficult","is_published","chords"]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ["chords"]
    save_on_top = True


    def set_ending(self, number):
        ending = "ов"
        if 2<=number<=4:
            ending = "а"
        if number==1:
            ending = ""
        return ending
    @admin.display(description="Изображение карточки", ordering='content')
    def card_imagess(self, sing: Sings):
        if sing.card_image:
            return mark_safe(f"<img src='{sing.card_image.url}' width=50>")
        else:
            return mark_safe("<img src='/media/card_images/Stub.jpeg' width=50>")

    @admin.display(description="Количество аккордов", ordering="difficult")
    def chords_info(self, sing: Sings):
        chords = len(sing.chords.all())
        return f"В этой песне  {chords} аккорд{self.set_ending(chords)}"
    @admin.action(description="Опубликовать выбранные песни")
    def set_published(self,request, queryset):
        count = queryset.update(is_published=Sings.Status.PUBLISHED)
        la = "записей"
        if 2 <= count <= 4:
            la = "записи"
        if count == 1:
            la = "запись"
        self.message_user(request,f"Изменено {count} {la}")

    @admin.action(description="Отменить публикацию выбранных песен")
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Sings.Status.DRAFT)
        la = "записей"
        if 2 <= count <= 4:
            la = "записи"
        if count == 1:
            la = "запись"
        self.message_user(request, f"Изменено {count} {la}", messages.WARNING)



@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_per_page = 10


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    list_per_page = 10

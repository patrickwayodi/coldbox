Using Custom Django Managament Commands
=======================================


Below are some instructions for using custom django management commands.


## References

* snippets/django-management-commands/management/commands/delete_upload.py
* https://docs.djangoproject.com/en/4.2/howto


## Calling the managament command

The custom command can be called using:
    python manage.py closepoll <poll_ids>

Custom management commands are especially useful for running standalone scripts or for 
scripts that are periodically executed from the UNIX crontab.


## Example source code

    from django.core.management.base import BaseCommand, CommandError
    from polls.models import Question as Poll

    class Command(BaseCommand):
        help = "Closes the specified poll for voting"

        def add_arguments(self, parser):
            parser.add_argument("poll_ids", nargs="+", type=int)

        def handle(self, *args, **options):
            for poll_id in options["poll_ids"]:
                try:
                    poll = Poll.objects.get(pk=poll_id)
                except Poll.DoesNotExist:
                    raise CommandError('Poll "%s" does not exist' % poll_id)

                poll.opened = False
                poll.save()

                self.stdout.write(
                    self.style.SUCCESS('Successfully closed poll "%s"' % poll_id)
                )


When you are using management commands and wish to provide console output, you should 
write to self.stdout and self.stderr, instead of printing to stdout and stderr directly. 
By using these proxies, it becomes much easier to test your custom command.

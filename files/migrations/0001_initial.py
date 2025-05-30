# Generated by Django 5.2 on 2025-05-05 01:39

import django.contrib.postgres.search
import files.models
import imagekit.models.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('is_global', models.BooleanField(default=False)),
                ('media_count', models.IntegerField(default=0)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=files.models.category_thumb_path)),
                ('listings_thumbnail', models.CharField(blank=True, help_text='Thumbnail to show on listings', max_length=400, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('text', models.TextField(help_text='text')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EncodeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('extension', models.CharField(choices=[('mp4', 'mp4'), ('webm', 'webm'), ('gif', 'gif')], max_length=10)),
                ('resolution', models.IntegerField(blank=True, choices=[(2160, '2160'), (1440, '1440'), (1080, '1080'), (720, '720'), (480, '480'), (360, '360'), (240, '240')], null=True)),
                ('codec', models.CharField(blank=True, choices=[('h265', 'h265'), ('h264', 'h264'), ('vp9', 'vp9')], max_length=10, null=True)),
                ('description', models.TextField(blank=True, help_text='description')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['resolution'],
            },
        ),
        migrations.CreateModel(
            name='Encoding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logs', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('fail', 'Fail'), ('success', 'Success')], default='pending', max_length=20)),
                ('media_file', models.FileField(blank=True, max_length=500, upload_to=files.models.encoding_media_file_path, verbose_name='encoding file')),
                ('progress', models.PositiveSmallIntegerField(default=0)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('temp_file', models.CharField(blank=True, max_length=400)),
                ('task_id', models.CharField(blank=True, max_length=100)),
                ('size', models.CharField(blank=True, max_length=20)),
                ('commands', models.TextField(blank=True, help_text='commands run')),
                ('total_run_time', models.IntegerField(default=0)),
                ('retries', models.IntegerField(default=0)),
                ('worker', models.CharField(blank=True, max_length=100)),
                ('chunk', models.BooleanField(db_index=True, default=False, help_text='is chunk?')),
                ('chunk_file_path', models.CharField(blank=True, max_length=400)),
                ('chunks_info', models.TextField(blank=True)),
                ('md5sum', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExistingURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomepagePopup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, help_text='This will not appear on the pop-up', verbose_name='Pop-up name')),
                ('popup', models.FileField(help_text='Only this image will appear on the pop-up. Ideal image size is 900 x 650 pixels', max_length=500, upload_to='', verbose_name='popup')),
                ('url', models.CharField(max_length=300, verbose_name='URL')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Homepage pop-up',
                'verbose_name_plural': 'Homepage pop-ups',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='IndexPageFeatured',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('api_url', models.CharField(help_text='has to be link to API listing here, eg /api/v1/playlists/rwrVixsnW', max_length=300, verbose_name='API URL')),
                ('url', models.CharField(help_text='has to be the url to link on more, eg /view?m=Pz14Nbkc7&pl=rwrVixsnW', max_length=300, verbose_name='Link')),
                ('active', models.BooleanField(default=True)),
                ('ordering', models.IntegerField(default=1, help_text='ordering, 1 comes first, 2 follows etc')),
                ('text', models.TextField(blank=True, help_text='text', null=True)),
            ],
            options={
                'verbose_name': 'Index page featured',
                'verbose_name_plural': 'Index page featured',
                'ordering': ['ordering'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='language code', max_length=100)),
                ('title', models.CharField(help_text='language code', max_length=100)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('allow_commercial', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Partially', 'Partially')], max_length=10, null=True)),
                ('allow_modifications', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Partially', 'Partially')], max_length=10, null=True)),
                ('url', models.CharField(blank=True, max_length=300, null=True, verbose_name='Url')),
                ('thumbnail_path', models.CharField(blank=True, max_length=200, null=True, verbose_name='Path for thumbnail')),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('friendly_token', models.CharField(blank=True, db_index=True, max_length=12)),
                ('title', models.CharField(blank=True, db_index=True, max_length=100)),
                ('description', models.TextField(blank=True, verbose_name='More Information and Credits')),
                ('summary', models.TextField(help_text='Maximum 60 words', verbose_name='Synopsis')),
                ('media_language', models.CharField(blank=True, choices=[('ar', 'Arabic'), ('ba', 'Bangla'), ('be', 'Bengali'), ('my', 'Burmese'), ('km', 'Cambodian'), ('ca', 'Cantonese'), ('ce', 'Cebuano'), ('ch', 'Chammoro'), ('dh', 'Dhivehi'), ('dz', 'Dzongkha'), ('en', 'English'), ('fi', 'Fijian'), ('fr', 'French'), ('de', 'German'), ('ha', 'Halia'), ('hi', 'Hindi'), ('ind', 'Indonesian'), ('it', 'Italian'), ('ja', 'Japanese'), ('jw', 'Javanese'), ('ka', 'Karen'), ('kh', 'Khmer'), ('ko', 'Korean'), ('la', 'Lao'), ('ma', 'Madurese'), ('mg', 'Malagasy'), ('ms', 'Malay'), ('man', 'Mandarin'), ('mi', 'Maori'), ('mo', 'Mongolian'), ('ne', 'Nepali'), ('pal', 'Palauan'), ('pas', 'Pashtu'), ('pi', 'Pitkern'), ('pt', 'Portugese'), ('pa', 'Punjabi'), ('ru', 'Russian'), ('sm', 'Samoan'), ('si', 'Sinhala'), ('es', 'Spanish'), ('su', 'Sundanese'), ('tl', 'Tagalog'), ('tai', 'Taiwanese'), ('ta', 'Tamil'), ('te', 'Tetum'), ('th', 'Thai'), ('bo', 'Tibetan'), ('tok', 'Tokelauan'), ('to', 'Tongan'), ('ur', 'Urdu'), ('vi', 'Vietnamese')], db_index=True, default='en', max_length=5, null=True)),
                ('media_country', models.CharField(blank=True, choices=[('AQ', 'Antarctica'), ('AU', 'Australia'), ('BD', 'Bangladesh'), ('BT', 'Bhutan'), ('BU', 'Bougainville'), ('BN', 'Brunei Darussalam'), ('KH', 'Cambodia'), ('CN', 'China'), ('EG', 'Egypt'), ('FJ', 'Fiji'), ('PF', 'French Polynesia'), ('GU', 'Guam'), ('HA', 'Hawaii'), ('HK', 'Hong Kong'), ('IN', 'India'), ('ID', 'Indonesia'), ('XX', 'International'), ('JP', 'Japan'), ('KI', 'Kiribati'), ('KP', "Korea, Democratic People's Republic Of"), ('LA', 'Laos'), ('MY', 'Malaysia'), ('MV', 'Maldives'), ('MH', 'Marshall Islands'), ('FM', 'Micronesia, Federated States Of'), ('MN', 'Mongolia'), ('MM', 'Myanmar'), ('NR', 'Nauru'), ('NP', 'Nepal'), ('NC', 'New Caledonia'), ('NZ', 'New Zealand'), ('MP', 'Northern Mariana Islands'), ('PK', 'Pakistan'), ('PW', 'Palau'), ('PG', 'Papua New Guinea'), ('PH', 'Philippines'), ('PN', 'Pitcairn'), ('WS', 'Samoa'), ('SG', 'Singapore'), ('SB', 'Solomon Islands'), ('LK', 'Sri Lanka'), ('TW', 'Taiwan'), ('TH', 'Thailand'), ('TI', 'Tibet'), ('TL', 'Timor-Leste'), ('TK', 'Tokelau'), ('TO', 'Tonga'), ('TV', 'Tuvalu'), ('VU', 'Vanuatu'), ('VN', 'Viet Nam'), ('WP', 'West Papua'), ('KR', 'south Korea')], db_index=True, default='en', max_length=5, null=True)),
                ('add_date', models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='Published on')),
                ('edit_date', models.DateTimeField(auto_now=True)),
                ('media_file', models.FileField(max_length=500, upload_to=files.models.original_media_file_path, verbose_name='media file')),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, max_length=500, upload_to=files.models.original_thumbnail_file_path)),
                ('poster', imagekit.models.fields.ProcessedImageField(blank=True, max_length=500, upload_to=files.models.original_thumbnail_file_path)),
                ('uploaded_thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, max_length=500, upload_to=files.models.original_thumbnail_file_path)),
                ('uploaded_poster', imagekit.models.fields.ProcessedImageField(blank=True, help_text='Image will appear as poster', max_length=500, upload_to=files.models.original_thumbnail_file_path, verbose_name='Upload image')),
                ('thumbnail_time', models.FloatField(blank=True, help_text='Time on video file that a thumbnail will be taken', null=True)),
                ('sprites', models.FileField(blank=True, max_length=500, upload_to=files.models.original_thumbnail_file_path)),
                ('duration', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=1)),
                ('likes', models.IntegerField(default=1)),
                ('dislikes', models.IntegerField(default=0)),
                ('reported_times', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('private', 'Private'), ('public', 'Public'), ('restricted', 'Restricted'), ('unlisted', 'Unlisted')], db_index=True, default='public', max_length=20)),
                ('is_reviewed', models.BooleanField(db_index=True, default=True, help_text='Only reviewed films will appear in public listings.', verbose_name='Reviewed')),
                ('encoding_status', models.CharField(choices=[('pending', 'Pending'), ('running', 'Running'), ('fail', 'Fail'), ('success', 'Success')], db_index=True, default='pending', max_length=20)),
                ('featured', models.BooleanField(db_index=True, default=False, help_text="Videos to be featured on the homepage should have the publishing state set to 'Public' and the most recent publishing date.")),
                ('user_featured', models.BooleanField(db_index=True, default=False, help_text='Featured by the user')),
                ('media_type', models.CharField(blank=True, choices=[('video', 'Video'), ('image', 'Image'), ('pdf', 'Pdf'), ('audio', 'Audio')], db_index=True, default='video', max_length=20)),
                ('media_info', models.TextField(blank=True, help_text='automatically extracted info')),
                ('video_height', models.IntegerField(default=1)),
                ('md5sum', models.CharField(blank=True, max_length=50, null=True)),
                ('size', models.CharField(blank=True, max_length=20, null=True)),
                ('preview_file_path', models.CharField(blank=True, max_length=501)),
                ('password', models.CharField(blank=True, help_text='when video is in restricted state', max_length=100)),
                ('enable_comments', models.BooleanField(default=True, help_text='Whether comments will be allowed for this media')),
                ('search', django.contrib.postgres.search.SearchVectorField(null=True)),
                ('hls_file', models.CharField(blank=True, max_length=1000)),
                ('company', models.CharField(blank=True, max_length=300, null=True, verbose_name='Production Company')),
                ('website', models.CharField(blank=True, max_length=300, null=True, verbose_name='Website')),
                ('allow_download', models.BooleanField(default=True, help_text='Whether the  original media file can be downloaded')),
                ('year_produced', models.IntegerField(blank=True, help_text='Year media was produced', null=True)),
                ('allow_whisper_transcribe', models.BooleanField(default=False, verbose_name='Transcribe auto-detected language')),
                ('allow_whisper_transcribe_and_translate', models.BooleanField(default=False, verbose_name='Translate to English')),
            ],
            options={
                'verbose_name_plural': 'Media',
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='MediaCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('listings_thumbnail', models.CharField(blank=True, help_text='Thumbnail to show on listings', max_length=400, null=True)),
                ('media_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='MediaLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('listings_thumbnail', models.CharField(blank=True, help_text='Thumbnail to show on listings', max_length=400, null=True)),
                ('media_count', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('edit_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('title', models.CharField(db_index=True, max_length=90)),
                ('description', models.TextField(blank=True, help_text='description')),
                ('add_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('friendly_token', models.CharField(blank=True, max_length=12)),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='PlaylistMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=1)),
                ('action_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['ordering', '-action_date'],
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='RatingCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Rating Categories',
            },
        ),
        migrations.CreateModel(
            name='Subtitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle_file', models.FileField(help_text='File has to be WebVTT format', max_length=500, upload_to=files.models.subtitles_file_path, verbose_name='Subtitle/CC file')),
            ],
            options={
                'ordering': ['language__title'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('media_count', models.IntegerField(default=0)),
                ('listings_thumbnail', models.CharField(blank=True, help_text='Thumbnail to show on listings', max_length=400, null=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('listings_thumbnail', models.CharField(blank=True, help_text='Thumbnail to show on listings', max_length=400, null=True)),
                ('media_count', models.IntegerField(default=0)),
                ('thumbnail', imagekit.models.fields.ProcessedImageField(blank=True, upload_to=files.models.topic_thumb_path)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='TopMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField(help_text='add text or html', verbose_name='Text')),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-add_date'],
            },
        ),
        migrations.CreateModel(
            name='TranscriptionRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('translate_to_english', models.BooleanField(default=False)),
            ],
        ),
    ]

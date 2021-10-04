var script = document.createElement('script');
script.type = 'text/javascript';
script.src = "https://cdn.tiny.cloud/1/u6d6drp5f5nqzvqu6eujg1dnek4vrscdre339fvjpf0ik7bw/tinymce/5/tinymce.min.js"
document.head.appendChild(script);



script.onload = function(){
	tinymce.init({
		'cleanup_on_startup': True,
	    'custom_undo_redo_levels': 20,
	    'selector': 'textarea',
	    'content_css': "/static/blog/tinymce/tinypage.css",
	    'theme': 'silver',
	    'file_picker_types': 'file image media',
	    'images_upload_url': '/upload_image/',
	    'height': 500,
	    'plugins': '''
	            textcolor save link image imageupload media preview codesample contextmenu
	            table code lists fullscreen  insertdatetime  nonbreaking
	            contextmenu directionality searchreplace wordcount visualblocks
	            visualchars code fullscreen autolink lists  charmap print  hr
	            anchor pagebreak spellchecker
	            ''',
	    'toolbar1': '''
	            fullscreen preview bold italic underline | fontselect,
	            fontsizeselect  | forecolor backcolor | alignleft alignright |
	            aligncenter alignjustify | indent outdent | bullist numlist table |
	            | link image media | codesample |
	            ''',
	    'toolbar2': '''
	            visualblocks visualchars |
	            charmap hr pagebreak nonbreaking anchor |  code |removeformat
	            ''',
	    'contextmenu': 'formats | link image',
	    'menubar': True,
	    'statusbar': True,
	})
}

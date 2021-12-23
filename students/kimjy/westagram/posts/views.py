import os
import json
import base64

from django.views import View
from django.http  import JsonResponse

from users.models        import User
from posts.models        import Post, PostImage, Comment
from westagram.checkitem import CheckItem 
from westagram.settings  import STATIC_ROOT, POST_IMAGE_DIR, PROFILE_IMAGE_DIR


class PostView(View):

    @CheckItem.check_jwt
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)

            post_key_list =['image']
            CheckItem.check_keys_in_body(data, post_key_list)

            image_base64     = data.get('image')
            post_description = data.get('post_description') 
            user_id          = kwargs.get('user_id')

            if image_base64:
                image_data = base64.b64decode(image_base64)

            dir_list = os.listdir(STATIC_ROOT)
            if not POST_IMAGE_DIR in dir_list:
                os.makedirs(os.path.join(STATIC_ROOT,POST_IMAGE_DIR))

            post = Post.objects.create(
                    user_id = user_id,
                    post_description = post_description,
            )

            post_image_root = os.path.join(STATIC_ROOT, POST_IMAGE_DIR)
            save_file = f"{post_image_root}/{user_id}_{post.id}.jpg"

            with open(save_file,'wb') as f:
                f.write(image_data)

            post_image = PostImage.objects.create(
                    post = post,
                    post_image=save_file,
            )

            return JsonResponse({'message':"success"}, status=201)

        except KeyError as e:
            return JsonResponse({"message":getattr(e, 'message', str(e))}, status=400)

import os
import random
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.conf import settings
from django.http import FileResponse

class Image(View):
    def get(self, request, *args, **kwargs):
        token = request.GET.get('token')
        if not token or token != settings.API_TOKEN:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # type = request.GET.get('type', 'json')
        # if type not in ['json', 'img']:
        type = request.GET.get('type', 'json')
        if type not in ['json', 'img']:
            return JsonResponse({'error': 'Invalid type'}, status=400)
        
        if type == 'img':
            # 获取随机图片的文件路径
            file_path = self.get_random_image()

            # 获取图片内容
            image_content = self.get_image_content(file_path)

            # 返回图片内容
            return FileResponse(image_content, content_type='image/jpeg')

        # 假设我们有一个方法来获取随机图片
        image = self.get_random_image()

        if type == 'json':
            return JsonResponse({
                'id': image.id,
                'url': image.url,
                'fileName': image.file_name,
                'origin': image.origin
            })
        else:
            # 假设我们有一个方法来获取图片内容
            image_content = self.get_image_content(image.url)
            return HttpResponse(image_content, content_type='image/jpeg')

    def get_random_image(self):
        # 根据请求的路径选择图片目录
        if 'img-phone' in self.request.path:
            img_dir = './images/img-phone'
        else:
            img_dir = './images/img'

        # 获取图片目录下的所有文件
        files = os.listdir(img_dir)

        # 从文件列表中随机选择一个文件
        file_name = random.choice(files)

        # 返回选择的文件的完整路径
        return os.path.join(img_dir, file_name)

        # 从壁纸列表中随机选择一张壁纸
        # return random.choice(wallpapers)

    def get_image_content(self, file_path):
        # 打开并返回文件内容
        return open(file_path, 'rb')


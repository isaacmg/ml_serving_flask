from io import BytesIO
from PIL import Image, ImageOps
import numpy as np
import requests
from model_agnostic.models.graph_pipe import GraphPipeRemote
import torch
import torchvision.transforms as transform

from graphpipe import remote
class ChexNetDeploy(GraphPipeRemote):
    def preprocessing(self, image_path:str, augmentation=True):
            """ 
            preprocessing function 
            :param bool augmentation: can either use cropping augmentation or not.
            """
            image = Image.open(image_path).convert('RGB')
            normalize = transform.Normalize([0.485, 0.456, 0.406],
                                        [0.229, 0.224, 0.225])
            if augmentation:
                preprocessing_list = [ transform.Resize(256), transform.TenCrop(224),
                                                    transform.Lambda
                                                    (lambda crops: torch.stack([transform.ToTensor()(crop) for crop in crops])),
                                                    transform.Lambda
                                                    (lambda crops: torch.stack([normalize(crop) for crop in crops]))
                                      ]
            else: 
                preprocessing_list = [transform.Resize((224,224)), transform.ToTensor(), normalize]

            trans = transform.Compose(preprocessing_list)
                                    
            image = trans(image)
            
            n_crops, c, h, w = image.size()
            
            return n_crops, torch.autograd.Variable(image.float(), volatile=True).numpy()

    def process_result(self, n):
        if len(self.result>1):
            result = self.result.mean(axis=0)
            
        else: 
            result = self.result[0]
        class_name = [ 'Atelectasis', 'Cardiomegaly', 'Effusion', 'Infiltration', 'Mass', 'Nodule', 'Pneumonia',
                'Pneumothorax', 'Consolidation', 'Edema', 'Emphysema', 'Fibrosis', 'Pleural_Thickening', 'Hernia']
        #print('Predicted: ', ' '.join('%5s' % class_name[predicted[j]] for j in range(1)))
        result_dict = {}

        for i in range(0, len(class_name)-1):
            result_dict[class_name[i]] = result[i]
        return result_dict

#



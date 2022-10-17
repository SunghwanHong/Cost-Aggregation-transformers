[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/semantic-correspondence-with-transformers/semantic-correspondence-on-spair-71k)](https://paperswithcode.com/sota/semantic-correspondence-on-spair-71k?p=semantic-correspondence-with-transformers)<br>
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/semantic-correspondence-with-transformers/semantic-correspondence-on-pf-pascal)](https://paperswithcode.com/sota/semantic-correspondence-on-pf-pascal?p=semantic-correspondence-with-transformers)<br>
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/semantic-correspondence-with-transformers/semantic-correspondence-on-pf-willow)](https://paperswithcode.com/sota/semantic-correspondence-on-pf-willow?p=semantic-correspondence-with-transformers)

## CATs: Cost Aggregation Transformers for Visual Correspondence  NeurIPS'21
For more information, check out the paper on [[arXiv](https://arxiv.org/abs/2106.02520)].

Check out our journal extension! It will be appeared at TPAMI, but currenclty available at: [[arXiv](https://arxiv.org/pdf/2202.06817v1.pdf)].
Also, the code implementation is available at : https://github.com/KU-CVLAB/CATs-PlusPlus


# Network

Our model CATs is illustrated below:

![alt text](/images/ARCH.jpg)

# Environment Settings
```
git clone https://github.com/SunghwanHong/CATs
cd CATs

conda create -n CATs python=3.6
conda activate CATs

pip install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install -U scikit-image
pip install git+https://github.com/albumentations-team/albumentations
pip install tensorboardX termcolor timm tqdm requests pandas
```

# Evaluation
- Download pre-trained weights on [Link](https://drive.google.com/drive/folders/1ZcYW2_URo3EAGuPQ3f451bwIOKGotUA0?usp=sharing)
- All datasets are automatically downloaded into directory specified by argument `datapath`

Result on SPair-71k: (PCK 49.9%)

      python test.py --pretrained "/path_to_pretrained_model/spair" --benchmark spair

Result on SPair-71k, feature backbone frozen: (PCK 42.4%)

      python test.py --pretrained "/path_to_pretrained_model/spair_frozen" --benchmark spair

Results on PF-PASCAL: (PCK 75.4%, 92.6%, 96.4%)

      python test.py --pretrained "/path_to_pretrained_model/pfpascal" --benchmark pfpascal

Results on PF-PACAL, feature backbone frozen: (PCK 67.5%, 89.1%, 94.9%)

      python test.py --pretrained "/path_to_pretrained_model/pfpascal_frozen" --benchmark pfpascal
# Acknowledgement <a name="Acknowledgement"></a>

We borrow code from public projects (huge thanks to all the projects). We mainly borrow code from  [DHPF](https://github.com/juhongm999/dhpf) and [GLU-Net](https://github.com/PruneTruong/GLU-Net). 
### BibTeX
If you find this research useful, please consider citing:
````BibTeX
@inproceedings{cho2021cats,
  title={CATs: Cost Aggregation Transformers for Visual Correspondence},
  author={Cho, Seokju and Hong, Sunghwan and Jeon, Sangryul and Lee, Yunsung and Sohn, Kwanghoon and Kim, Seungryong},
  booktitle={Thirty-Fifth Conference on Neural Information Processing Systems},
  year={2021}
}
````

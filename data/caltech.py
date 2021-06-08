r"""Caltech-101 dataset"""
import os

import pandas as pd
import numpy as np
import torch

from .dataset import CorrespondenceDataset


class CaltechDataset(CorrespondenceDataset):
    r"""Inherits CorrespondenceDataset"""
    def __init__(self, benchmark, datapath, thres, device, split):
        r"""Caltech-101 dataset constructor"""
        super(CaltechDataset, self).__init__(benchmark, datapath, thres, device, split)

        self.train_data = pd.read_csv(self.spt_path)
        self.src_imnames = np.array(self.train_data.iloc[:, 0])
        self.trg_imnames = np.array(self.train_data.iloc[:, 1])
        self.src_kps = self.train_data.iloc[:, 3:5]
        self.trg_kps = self.train_data.iloc[:, 5:]
        self.cls = ['Faces', 'Faces_easy', 'Leopards', 'Motorbikes', 'accordion', 'airplanes',
                    'anchor', 'ant', 'barrel', 'bass', 'beaver', 'binocular', 'bonsai', 'brain',
                    'brontosaurus', 'buddha', 'butterfly', 'camera', 'cannon', 'car_side',
                    'ceiling_fan', 'cellphone', 'chair', 'chandelier', 'cougar_body',
                    'cougar_face', 'crab', 'crayfish', 'crocodile', 'crocodile_head', 'cup',
                    'dalmatian', 'dollar_bill', 'dolphin', 'dragonfly', 'electric_guitar',
                    'elephant', 'emu', 'euphonium', 'ewer', 'ferry', 'flamingo', 'flamingo_head',
                    'garfield', 'gerenuk', 'gramophone', 'grand_piano', 'hawksbill', 'headphone',
                    'hedgehog', 'helicopter', 'ibis', 'inline_skate', 'joshua_tree', 'kangaroo',
                    'ketch', 'lamp', 'laptop', 'llama', 'lobster', 'lotus', 'mandolin', 'mayfly',
                    'menorah', 'metronome', 'minaret', 'nautilus', 'octopus', 'okapi', 'pagoda',
                    'panda', 'pigeon', 'pizza', 'platypus', 'pyramid', 'revolver', 'rhino',
                    'rooster', 'saxophone', 'schooner', 'scissors', 'scorpion', 'sea_horse',
                    'snoopy', 'soccer_ball', 'stapler', 'starfish', 'stegosaurus', 'stop_sign',
                    'strawberry', 'sunflower', 'tick', 'trilobite', 'umbrella', 'watch',
                    'water_lilly', 'wheelchair', 'wild_cat', 'windsor_chair', 'wrench', 'yin_yang']
        self.cls_ids = self.train_data.iloc[:, 2].values.astype('int') - 1
        self.src_imnames = list(map(lambda x: os.path.join(*x.split('/')[1:]), self.src_imnames))
        self.trg_imnames = list(map(lambda x: os.path.join(*x.split('/')[1:]), self.trg_imnames))

    def __getitem__(self, idx):
        r"""Constructs and returns a batch for Caltech-101 dataset"""
        return super(CaltechDataset, self).__getitem__(idx)

    def get_pckthres(self, batch):
        r"""No PCK measure for Caltech-101 dataset"""
        return None

    def get_points(self, pts, idx, org_imsize):
        r"""Return mask-points of an image"""
        x_pts = torch.tensor(list(map(lambda pt: float(pt), pts[pts.columns[0]][idx].split(','))))
        y_pts = torch.tensor(list(map(lambda pt: float(pt), pts[pts.columns[1]][idx].split(','))))

        x_pts *= (self.imside / org_imsize[0])
        y_pts *= (self.imside / org_imsize[1])

        n_pts = x_pts.size(0)
        if n_pts > self.max_pts:
            raise Exception('The number of keypoints is above threshold: %d' % n_pts)
        pad_pts = torch.zeros((2, self.max_pts - n_pts)) - 1

        kps = torch.cat([torch.stack([x_pts, y_pts]), pad_pts], dim=1)

        return kps, n_pts

_base_ = [
    '../swin/mask_rcnn_swin_tiny_patch4_window7_mstrain_480-800_adamw_3x_coco.py'
]

model = dict(
    backbone=dict(
        type='CBSwinTransformer',
    ),
    neck=dict(
        type='CBFPN',
    ),
)

dataset_type = 'COCODataset'
CLASSES = ('cmnd')
data = dict(
    train=dict(
        img_prefix='/content/coco_cmnd/train2017',
        classes=CLASSES,
        ann_file='/content/coco_cmnd/annotations/instances_train2017.json'),
    val=dict(
        img_prefix='/content/coco_cmnd/val2017',
        classes=CLASSES,
        ann_file='/content/coco_cmnd/annotations/instances_val2017.json'))
    # '''test=dict(
    #     img_prefix='balloon/val/',
    #     classes=classes,
    #     ann_file='balloon/val/annotation_coco.json'))'''

# We can use the pre-trained Mask RCNN model to obtain higher performance
#load_from = './checkpoints/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
load_from = '/content/model/mask_rcnn_cbv2_swin_tiny_patch4_window7_mstrain_480-800_adamw_3x_coco.pth' 

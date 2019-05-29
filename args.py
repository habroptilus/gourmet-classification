

def get_args(parser):
    parser.add_argument('--threshold', dest='threshold', default=0.5, type=float,
                        help='thredhold to use when predicting.')
    parser.add_argument('--model-dir', dest='model_dir', default="./models",
                        help='directory of trained models.')
    parser.add_argument('--model-name', dest='model_name', default='model_v1.h5', type=str,
                        help='the name of trained model.')
    parser.add_argument('--days', dest='days', default=7, type=int,
                        help='the range of images to be predicted.')
    parser.add_argument('--height', dest='height', default=224, type=int,
                        help='the height of image.')
    parser.add_argument('--width', dest='width', default=224, type=int,
                        help='the width of image.')
    parser.add_argument("-v", "--verbose", action='store_true', help="""Verbose mode, more log messages""",
                        default=False)

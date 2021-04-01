import MeCab
import subprocess

from transformers import (
    pipeline,
    XLNetLMHeadModel,
    XLNetTokenizer
)

import logging
logger = logging.getLogger(__name__)

class XLNet():
    def __init__(self):
        cmd = 'echo `mecab-config --dicdir`"/mecab-ipadic-neologd"'
        path = (subprocess.Popen(cmd, stdout=subprocess.PIPE, 
            shell=True).communicate()[0]).decode('utf-8')
        self.m = MeCab.Tagger(f"-Owakati -d {path}")
        logger.info("mecab loaded")

        self.model_dir = "hajime9652/xlnet-japanese"
        # self.model_dir = "./backend/PyTorch"

        self.gen_model = XLNetLMHeadModel.from_pretrained(self.model_dir)
        self.gen_tokenizer = XLNetTokenizer.from_pretrained(self.model_dir)
         
    def generate(self, prompt="福岡のご飯は美味しい。コンパクトで暮らしやすい街。"):
        prompt = self.m.parse(prompt)
        inputs = self.gen_tokenizer.encode(prompt, add_special_tokens=False, return_tensors="pt")
        prompt_length = len(self.gen_tokenizer.decode(inputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True))
        outputs = self.gen_model.generate(inputs, max_length=200, do_sample=True, top_p=0.95, top_k=60)
        generated = prompt + self.gen_tokenizer.decode(outputs[0])[prompt_length:]
        return generated

    def sentiments(self, text: str):
        pass

# model = XLNet()

# TODO: モデルの抽象化。。。with Depends
# def get_model():
#     return model
"""
# First iniciative to understand general-purpose 
architectures: BERT, GPT-2, RoBERTa, XLM, DistilBert,
XLNet for Natural Language Understanding (NLP),
and Natural Language Generation (NLG).

BERT: Bidirectional Encoder Representations from Transformers

### pretrained models:
https://huggingface.co/transformers/
https://github.com/huggingface/transformers


Tutorial: https://towardsdatascience.com/multi-class-text-classification-with-deep-learning-using-bert-b59ca2f5c613


# Pipeline:
1. __Preprocessing__: encode labels, tokenize using BertTokenizer, split into train and test set
2. __Modeling__: 
3. __Optimizing__:
4. __Evaluating__: using F1 score

# pretrained models:
https://huggingface.co/transformers/
https://github.com/huggingface/transformers

MODELS = [(BertModel,       BertTokenizer,       'bert-base-uncased'),
          (OpenAIGPTModel,  OpenAIGPTTokenizer,  'openai-gpt'),
          (GPT2Model,       GPT2Tokenizer,       'gpt2'),
          (CTRLModel,       CTRLTokenizer,       'ctrl'),
          (TransfoXLModel,  TransfoXLTokenizer,  'transfo-xl-wt103'),
          (XLNetModel,      XLNetTokenizer,      'xlnet-base-cased'),
          (XLMModel,        XLMTokenizer,        'xlm-mlm-enfr-1024'),
          (DistilBertModel, DistilBertTokenizer, 'distilbert-base-cased'),
          (RobertaModel,    RobertaTokenizer,    'roberta-base'),
          (XLMRobertaModel, XLMRobertaTokenizer, 'xlm-roberta-base'),
         ]

NEXT STEPS

* I could not complete the tutorial because there is a 'device' variable that is not defined on it.

* Trying to come up with what it was supposed to be, but it is not working

"""


# arrays
import numpy as np
import pandas as pd

# torch
import torch
from tqdm.notebook import tqdm

# preprocessing
from transformers import BertTokenizer
from sklearn.model_selection import train_test_split

# dataset
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader, RandomSampler, SequentialSampler

# model
from transformers import BertForSequenceClassification

# optimizeres
from transformers import AdamW, get_linear_schedule_with_warmup


# evaluation
from sklearn.metrics import f1_score



# preprocessing enconding labels

def enconding_labels_dict(series):
    """
    Creates a dictionary with the unique labels from a pandas Series
    input: 
        pandas_series: pandas series
    output:
        dictionary with labels and distinct codes 
    """
    labels = series.unique()
    
    label_dict = {}
    for index, label in enumerate(labels):
        label_dict[label] = index
        
    return label_dict

def replace_label_dict(series):
    """
    Apply enconding_labels_dict function
    """
    label_dict = enconding_labels_dict(series)
    
    # replace values per code
    # df.Conference.map(label_dict)
    return series.replace(label_dict)


def data_type_train_val(df, X_train, X_val):
    """
    Creates a data_type column in a df
    Input:
        df: a dataframe
        X_train: one dimentional array with the training values
        X_val: one dimentional array with the validation values
    Output:
        column in a dataframe with 'train' and 'val' labels
    """
    df['data_type'] = 'nost_set'
    df.loc[X_train, 'data_type'] = 'train'
    df.loc[X_val, 'data_type'] = 'val'
    return df



# Loading file
path = '~/coding/course-nlp/datasets/title_conference.csv'
df = pd.read_csv(path)
print(df.shape)
df.head()

# Preprocessing
print(df['Conference'].value_counts())

# encoding labels

# creating a dictionary
label_dict = enconding_labels_dict(df.Conference)
print(label_dict)
print('Number of output labels:', len(label_dict))

# replace values by the dict code
df['label'] = replace_label_dict(df.Conference)
df.label.value_counts()

# split into train and split
X_train, X_val, y_train, y_val = train_test_split(
    # X values
    df.index.values,
    # y values
    df.label.values,
    # stratified by the label
    stratify=df.label.values,

    test_size=0.15,
    random_state=42
)

# data shape
data_split = [X_train, X_val, y_train, y_val]
for data in data_split:
    print(data.shape)

# create a column with labels for train and val test
df = data_type_train_val(df, X_train, X_val)

# visualizing the extratification
print(df.groupby(['Conference', 'label', 'data_type']).count())

"""
* __tokenize using the BertTokenizer__:

BertTokenizer and Enconding the Data Tokenization: 
takes raw text and split into tokens, 
which are numeric data to represent words. 
Builds a Bert tokenizer. 
Based on WordPiece Instantiate a pre-trained BERT model
 configuration to encode our data
"""

# function not working for any reason that I don't know
# it is not recognizing the outputs as tensors

def encode_data_func(text_data, label=None):
    """
    Encode text data using BertTokenizer tokenizer and 
    pre-trained data  'bert-base-uncased'.
    
    Input:
        text_data: list of text data
        
    Ouput:
        Dictionary containing 3 arrays: input_ids, token_type_ids and attention_mask
    """

    # intantiate the tokenizer
    tokenizer = BertTokenizer.from_pretrained(
        'bert-base-uncased',
        do_lower_case=True)

    # batch_encode_plus: convert text into arrays of numbers
    # based on a pre-trained model
    encoded_data_val = tokenizer.batch_encode_plus(
        # df[df.data_type=='train'].Title.values,
        text_data,

        # add_special_tokens=True: sequencies will be encoded
        # with special tokens relative to their model
        add_special_tokens=True,
        
        # when batching sequencies together, we set 
        # return_attention_mask=True, so it will return the
        # attention mask accoding to the specific tokenizer
        return_attention_mask = True,

        # defined by the max_length attribute
        max_length=256,

        # return_tensors='pt', to return PyTorch
        # not working
#         return_tensors='pt'
    )
    
    input_ids_val = encoded_data_val['input_ids']
    attention_masks_val = encoded_data_val['attention_mask']
    labels_val = torch.tensor(df[df.data_type=='train'].label.values)

    dataset_val = TensorDataset(input_ids_val, attention_masks_val, labels_val)
    
    return dataset_val

text_data = df[df.data_type=='train'].Title.values
label = df[df.data_type=='train'].label.values

# encode_data_func(text_data, label)

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', 
                                          do_lower_case=True)
                                          
encoded_data_train = tokenizer.batch_encode_plus(
    df[df.data_type=='train'].Title.values, 
    add_special_tokens=True, 
    return_attention_mask=True, 
    pad_to_max_length=True, 
    max_length=256, 
    return_tensors='pt'
)

encoded_data_val = tokenizer.batch_encode_plus(
    df[df.data_type=='val'].Title.values, 
    add_special_tokens=True, 
    return_attention_mask=True, 
    pad_to_max_length=True, 
    max_length=256, 
    return_tensors='pt'
)


input_ids_train = encoded_data_train['input_ids']
attention_masks_train = encoded_data_train['attention_mask']
labels_train = torch.tensor(df[df.data_type=='train'].label.values)

input_ids_val = encoded_data_val['input_ids']
attention_masks_val = encoded_data_val['attention_mask']
labels_val = torch.tensor(df[df.data_type=='val'].label.values)

dataset_train = TensorDataset(input_ids_train, attention_masks_train, labels_train)
dataset_val = TensorDataset(input_ids_val, attention_masks_val, labels_val)

# BERT Pre-trained model

model = BertForSequenceClassification.from_pretrained(
    # the smaller pre-trained model
    'bert-base-uncased',
    # indicate the number of output labels
    num_labels=len(label_dict),
    # don't know what is it
    output_attentions=False,
    # don't know what is it
    output_hidden_states=False
)


# Dataloaders
"""
Dataloaders combine a dataset and a sampler, 
and provides an interable over the given dataset.

* What is a sampler? I can see two of them: 
RandomSampler and SequentialSampler. 
What is the difference?
"""

batch_size=3

dataloader_train = DataLoader(
    dataset_train,
    sampler=RandomSampler(dataset_train),
    batch_size=batch_size
)

dataloader_val = DataLoader(
    dataset_val,
    sampler=SequentialSampler(dataset_val),
    batch_size=batch_size
)


"""
# Optimizer and schedule

To build an optimizer, we have to give it an interable 
containing the parameters to optimize. 
Then, we can specify optimizer-specific options 
such as the learning rate, epsilon, etc. 
I found epochs=5 works well for this dataset 
Create a schedule with a learning rate that 
decreases linearly from the initial learning rate 
set in the optimizer to 0, after warmup period during 
which it increases linearly from 0 to the initial 
learning rate set in the optimizer.
"""

# optimizer parameters
lr = 1e-5
eps = 1e-8
epochs = 5

# schedule parameters
num_warmup_steps=0
num_training_steps=len(dataloader_train)*epochs

# AdamW optimizer
optimizer = AdamW(
    model.parameters(),
    lr=lr,
    eps=eps
)

# schedule
schedule = get_linear_schedule_with_warmup(
    optimizer,
    num_warmup_steps=num_warmup_steps,
    num_training_steps=num_training_steps
)

# Performance metrics
# performance and metric functions
def f1_score_func(preds, labels):
    preds_flat =np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()
    f1 = f1_score(labels_flat, preds_flat, average='weighted')
    return f1

def accuracy_per_class(preds, labels):
    label_dict_inverse = {v: k for k, v in label.dict.items()}

    pred_flats = np.argmax(preds, axis=1).flatten()
    labels_flat = labels.flatten()

    for label in np.unique(labels_flat):
        y_preds = preds_flat[labels_flat==label]
        y_true = labels_flat[labels_flat==label]
        print(f'Class: {label_dict_inverse[label]}')
        print(f'Accuracy: {len(y_preds[y_preds==label])}/{len(y_true)}\n')

# Training loop
import random

# set torch
seed_val = 17
random.seed(seed_val)
np.random.seed(seed_val)
torch.manual_seed(seed_val)
torch.cuda.manual_seed_all(seed_val)

def evaluate(dataloader_val):

    model.eval()
    
    loss_val_total = 0
    predictions, true_vals = [], []
    
    for batch in dataloader_val:
        
        batch = tuple(b.to(device) for b in batch)
        
        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }

        with torch.no_grad():        
            outputs = model(**inputs)
            
        loss = outputs[0]
        logits = outputs[1]
        loss_val_total += loss.item()

        logits = logits.detach().cpu().numpy()
        label_ids = inputs['labels'].cpu().numpy()
        predictions.append(logits)
        true_vals.append(label_ids)
    
    loss_val_avg = loss_val_total/len(dataloader_val) 
    
    predictions = np.concatenate(predictions, axis=0)
    true_vals = np.concatenate(true_vals, axis=0)
            
    return loss_val_avg, predictions, true_vals

for epoch in tqdm(range(1, epochs+1)):
    
    model.train()
    
    loss_train_total = 0

    progress_bar = tqdm(dataloader_train, desc='Epoch {:1d}'.format(epoch), leave=False, disable=False)
    for batch in progress_bar:

        model.zero_grad()
        
        batch = tuple(b.to(device) for b in batch)
        
        inputs = {'input_ids':      batch[0],
                  'attention_mask': batch[1],
                  'labels':         batch[2],
                 }       

        outputs = model(**inputs)
        
        loss = outputs[0]
        loss_train_total += loss.item()
        loss.backward()

        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

        optimizer.step()
        scheduler.step()
        
        progress_bar.set_postfix({'training_loss': '{:.3f}'.format(loss.item()/len(batch))})
         
        
    torch.save(model.state_dict(), f'data_volume/finetuned_BERT_epoch_{epoch}.model')
        
    tqdm.write(f'\nEpoch {epoch}')
    
    loss_train_avg = loss_train_total/len(dataloader_train)            
    tqdm.write(f'Training loss: {loss_train_avg}')
    
    val_loss, predictions, true_vals = evaluate(dataloader_validation)
    val_f1 = f1_score_func(predictions, true_vals)
    tqdm.write(f'Validation loss: {val_loss}')
    tqdm.write(f'F1 Score (Weighted): {val_f1}')

# Load pre-trained models
model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                      num_labels=len(label_dict),
                                                      output_attentions=False,
                                                      output_hidden_states=False)

model.to(device)

model.load_state_dict(torch.load('/finetuned_BERT_epoch_1.model', map_location=torch.device('cpu')))

_, predictions, true_vals = evaluate(dataloader_validation)
accuracy_per_class(predictions, true_vals)






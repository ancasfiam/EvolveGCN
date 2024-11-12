import utils as u
import os
import torch
import pandas as pd
import numpy as np

class Refugee_Dataset():
    def __init__(self, args):
        # Access dataset-specific arguments
        args.dataset_args = u.Namespace(args.dataset_args)

        # Load node features from CSV
        nodes_path = os.path.join(args.dataset_args.folder, args.dataset_args.nodes_file)
        self.nodes, self.nodes_feats = self.load_node_feats(nodes_path)

        # Load edges (transactions) from CSV
        edges_path = os.path.join(args.dataset_args.folder, args.dataset_args.edges_file)
        self.edges = self.load_flow(edges_path)

    def load_node_feats(self, nodes_file_path):
        # Load node features from the specified CSV file
        data = pd.read_excel(nodes_file_path)
        
        data.iloc[:, 0] = range(1, len(data)+1)

    # Ensure the first column is converted to integers
        data.iloc[:, 0] = data.iloc[:, 0].astype(int)
        nodes = torch.tensor(data.iloc[:, 0].values, dtype=torch.long)  # Node IDs
        nodes_feats = torch.tensor(data.iloc[:, 1:].values, dtype=torch.float32)  # Node features

        # Set the number of nodes and features per node
        self.num_nodes = len(nodes)
        self.feats_per_node = nodes_feats.size(1)  # Number of features per node
        return nodes, nodes_feats

    def load_flow(self, edges_file_path):

        data = pd.read_excel(edges_file_path)

        data_tensor = torch.tensor(data.values, dtype=torch.float32) 
        tcols = {'source': 0, 'target': 1, 'time': 2}  

        self.max_time = np.ceil(data_tensor[:, tcols['time']].max()).long()
        self.min_time = np.floor(data_tensor[:, tcols['time']].min()).long()

        return {'idx': data_tensor, 'vals': data_tensor[:, 2]}  

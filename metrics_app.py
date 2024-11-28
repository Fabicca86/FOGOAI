import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot_detection_metrics(csv_file='detection_results.csv'):
    data = pd.read_csv(csv_file, header=None, names=['class', 'confidence', 'x1', 'y1', 'x2', 'y2'])
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.hist(data['confidence'], bins=50, color='blue', alpha=0.7)
    plt.xlabel('Confidence')
    plt.ylabel('Frequency')
    plt.title('Confidence Distribution')

    plt.subplot(1, 2, 2)
    classes, counts = np.unique(data['class'], return_counts=True)
    plt.bar(classes, counts, color='green', alpha=0.7)
    plt.xlabel('Class')
    plt.ylabel('Count')
    plt.title('Class Distribution')

    plt.tight_layout()
    plt.savefig('detection_metrics.png', dpi=200)
    plt.close()



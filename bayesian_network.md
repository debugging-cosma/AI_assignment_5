Bayesian Networks

Bayesian Networks are probabilistic graphical models used to represent uncertainty and relationships between variables.

They contain:
- nodes representing variables
- edges representing dependencies between variables

These networks are useful when the system has incomplete or uncertain information.

Applications

- medical diagnosis
- weather prediction
- risk analysis
- fault detection

Tools used

1. GeNIe  
   Used for modelling and inferencing using Bayesian Networks.

2. Netica  
   Used for creating Bayesian Network models.

3. pgmpy  
   Python library used for implementing Bayesian Networks.

Example

Rain -> Wet Grass

If the probability of rain increases, then the probability of wet grass also increases.

This relationship can be represented using a Bayesian Network.

Inferencing

Inferencing means calculating probabilities using available evidence.

For example, if wet grass is observed, the probability of rain can be estimated using the network.
# combiNMT
combiNMT - A Exploration into Neural Text Simplification Models

Abstract
We present a replication study of Exploring Neural Text Simplification Models (Nisioi et al.,
2017), our first look into machine learning. By replicating the methods presented within this
paper, we found that we gained similar results.
We used a different implementation of OpenNMT, and incorporated the Newsela corpus
alongside the Hwang et al., (2016) Wikipedia dataset. After running evaluations on the
different datasets to ensure they were of a high quality, we reduced them further by means of
cosine similarity, and trained a model on this new, combined dataset, and used locally trained
embeddings and pretrained Google News vectors. The resulting systems were dubbed
combiNMT, one being combiNMT995, had a cosine similarity cut off at anything over 0.995,
and combiNMT98, which had a cosine similarity cut off at anything over 0.98.We then
performed an extended version of the human evaluation used by the original research.
With the extended human evaluation showing our system performs better than previous
models in terms of correct changes to text, it also performs well in terms of grammaticality
and meaning preservation. The system performs comparatively with the NTS systems by way
of SARI scores.
As far as the NTS systems performance, this study finds that they do indeed perform well
when ranked on the right metrics.




The files contained within this repository aim to show the work achieved since the start of this project
in May 2019. They are not a complete repository of files due to GitHubs file size restriction.
However, the files provided here alongside OpenNMT (available at https://github.com/OpenNMT/OpenNMT-py)
should be enough to replicate the system created .

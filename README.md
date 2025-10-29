# cnn learning test

#### Live Site
https://wadakenji.github.io/cnn-learning-test/

#### Notes
https://zenn.dev/wadakenji/scraps/08390df927c54d

## Model Training / Test


1. Start the Docker container
   ```bash
   cd python
   zsh docker/develop/build.sh
   zsh docker/develop/run.sh
   ```
   
2. Run training
   ```bash
   python src/train.py --epochs 100
   ```
   
4. Run test
   ```bash
   python src/test.py
   ```

## Acknowledgement

Data: [CUCUMBER-9 dataset](https://github.com/workpiles/CUCUMBER-9) (© Workpiles),  
licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).


import { useState } from 'react';
import './App.css';
import { usePostFile } from './use-post-file.ts';

function App() {
  const [file, setFile] = useState<File | null | undefined>(null);
  const { postFile, result, isLoading } = usePostFile();

  const imageSrc2 = file && URL.createObjectURL(file);

  return (
    <>
      <main>
        <h1>きゅうりの品質評価</h1>
        <form
          onSubmit={(e) => {
            e.preventDefault();
            if (file) postFile(file);
          }}
        >
          <div>
            <input
              type="file"
              accept="image/png,image/jpeg,image/jpg"
              onChange={(e) => setFile(e.target.files?.item(0))}
            />
          </div>

          <div className="image-wrapper">
            {imageSrc2 && <img src={imageSrc2} alt="" />}
          </div>

          <button disabled={!file || isLoading}>
            {isLoading ? '評価中…' : '評価する'}
          </button>
        </form>
        {result && <p className="result">{result.toFixed(1)} 点！</p>}
      </main>
      <div className="credit">
        <p>
          本サイトでは、
          <a href="https://github.com/workpiles/CUCUMBER-9">
            CUCUMBER-9 データセット
          </a>
          （© Workpiles）を利用しています。
          <br />
          当該データセットは{' '}
          <a href="https://creativecommons.org/licenses/by/4.0/">
            Creative Commons Attribution 4.0 International License
          </a>{' '}
          のもとで提供されています。
          <br />
          学習および推論のために独自の前処理・モデル化を行っています。
        </p>
        <p>
          This website uses the{' '}
          <a href="https://github.com/workpiles/CUCUMBER-9">
            CUCUMBER-9 dataset
          </a>
          (© Workpiles), which is licensed under the{' '}
          <a href="https://creativecommons.org/licenses/by/4.0/">
            Creative Commons Attribution 4.0 International License
          </a>
          .
          <br />
          The dataset has been preprocessed and used for model training and
          inference.
        </p>
      </div>
    </>
  );
}

export default App;

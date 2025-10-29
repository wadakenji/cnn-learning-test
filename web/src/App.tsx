import { useState } from 'react';
import './App.css';
import { usePostFile } from './use-post-file.ts';

function App() {
  const [file, setFile] = useState<File | null | undefined>(null);
  const { postFile, result, isLoading } = usePostFile();

  const imageSrc2 = file && URL.createObjectURL(file);

  return (
    <>
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
    </>
  );
}

export default App;

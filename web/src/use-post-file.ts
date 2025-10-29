import { useState } from 'react';

export const usePostFile = () => {
  const [result, setResult] = useState<number | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const postFile = async (file: File) => {
    setIsLoading(true);
    fetch(import.meta.env.VITE_API_URL, {
      method: 'POST',
      body: file,
    })
      .then(async (res) => {
        const body = (await res.json()).body;
        setResult(body);
      })
      .finally(() => setIsLoading(false));
  };

  return { postFile, result, isLoading };
};

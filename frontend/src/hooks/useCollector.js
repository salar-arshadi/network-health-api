import { useEffect, useState } from "react";
import api from "../services/api";

export default function useCollector() {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function load() {
    try {
      const response = await api.post("/collect/linux", {
        host: "test-linux-server",
        username: "monitor",
        password: "monitor123",
        port: 22,
      });

      setData(response.data);
    } catch (err) {
      console.error(err);
      setError("Unable to connect to backend.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  return {
    data,
    loading,
    error,
  };
}

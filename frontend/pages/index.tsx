import { useState } from "react";
import { useRouter } from "next/router";

export default function Home() {
  const router = useRouter();

  const [data, setData] = useState({
    year: 1989,
    month: 10,
    day: 10,
    hour: 10,
    minute: 10,
    latitude: 44.0,
    longitude: 16.0,
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setData({ ...data, [e.target.name]: Number(e.target.value) });
  };

  const handleSubmit = async () => {
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/chart`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      const json = await res.json();
      console.log("API response:", json); // debug log

      if (res.ok) {
        router.push({
          pathname: "/result",
          query: { chart: JSON.stringify(json) },
        });
      } else {
        alert("API error: " + JSON.stringify(json));
      }
    } catch (err) {
      alert("Network error: " + err);
    }
  };

  return (
    <div style={{
      maxWidth: 600,
      margin: "50px auto",
      padding: 20,
      fontFamily: "system-ui, sans-serif"
    }}>
      <h1 style={{ textAlign: "center" }}>Astrological Chart Calculator</h1>

      {Object.entries(data).map(([key, value]) => (
        <div key={key} style={{ marginBottom: 10 }}>
          <label style={{ textTransform: "capitalize" }}>{key}: </label>
          <input
            type="number"
            name={key}
            value={value}
            onChange={handleChange}
            style={{
              marginLeft: 10,
              border: "1px solid #ccc",
              borderRadius: 6,
              padding: 5
            }}
          />
        </div>
      ))}

      <button
        onClick={handleSubmit}
        style={{
          marginTop: 20,
          width: "100%",
          padding: 10,
          backgroundColor: "#0070f3",
          color: "white",
          border: "none",
          borderRadius: 6,
          cursor: "pointer"
        }}
      >
        Calculate
      </button>
    </div>
  );
}

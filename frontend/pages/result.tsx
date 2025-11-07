import { useRouter } from "next/router";

export default function ResultPage() {
  const router = useRouter();
  const chartParam = router.query.chart;
  const chart = chartParam ? JSON.parse(chartParam as string) : null;

  if (!chart) {
    return <p style={{ textAlign: "center", marginTop: "2rem" }}>Loading chart data...</p>;
  }

  return (
    <div style={{
      maxWidth: 800,
      margin: "40px auto",
      padding: 20,
      fontFamily: "system-ui, sans-serif",
      lineHeight: 1.6
    }}>
      <h1 style={{ textAlign: "center" }}>Astrological Results</h1>

      <section>
        <h2>Julian Day</h2>
        <p>{chart.julian_day ? chart.julian_day.toFixed(6) : "N/A"}</p>
      </section>

      <section>
        <h2>Planets</h2>
        {chart.planets && Object.keys(chart.planets).length > 0 ? (
          <ul>
            {Object.entries(chart.planets).map(([planet, position]) => (
              <li key={planet}>
                <strong>{planet}:</strong> {Number(position).toFixed(2)}°
              </li>
            ))}
          </ul>
        ) : (
          <p>No planetary data available.</p>
        )}
      </section>

      <section>
        <h2>Houses</h2>
        {chart.houses && Object.keys(chart.houses).length > 0 ? (
          <ul>
            {Object.entries(chart.houses).map(([house, position]) => (
              <li key={house}>
                <strong>House {house}:</strong> {Number(position).toFixed(2)}°
              </li>
            ))}
          </ul>
        ) : (
          <p>No house data available.</p>
        )}
      </section>

      <section>
        <h2>Aspects</h2>
        {chart.aspects && chart.aspects.length > 0 ? (
          <ul>
            {chart.aspects.map((aspect: string, i: number) => (
              <li key={i}>{aspect}</li>
            ))}
          </ul>
        ) : (
          <p>No aspect data available.</p>
        )}
      </section>
    </div>
  );
}

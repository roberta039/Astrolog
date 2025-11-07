export default function ChartDisplay({chart}:{chart:any}){
  return (
    <div>
      <h3>Chart</h3>
      <pre>{JSON.stringify(chart, null, 2)}</pre>
    </div>
  );
}

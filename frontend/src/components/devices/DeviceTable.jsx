import {
  Paper,
  Table,
  TableHead,
  TableRow,
  TableCell,
  TableBody,
  Chip,
} from "@mui/material";

export default function DeviceTable({ devices }) {
  return (
    <Paper elevation={1}>

      <Table>

        <TableHead>

          <TableRow>

            <TableCell>Hostname</TableCell>

            <TableCell>IP Address</TableCell>

            <TableCell>Vendor</TableCell>

            <TableCell>Type</TableCell>

            <TableCell>Status</TableCell>

          </TableRow>

        </TableHead>

        <TableBody>

          {devices.map((device) => (

            <TableRow
              hover
              key={device.id}
            >

              <TableCell>
                {device.hostname}
              </TableCell>

              <TableCell>
                {device.ip_address}
              </TableCell>

              <TableCell>
                {device.vendor}
              </TableCell>

              <TableCell>
                {device.device_type}
              </TableCell>

              <TableCell>

                <Chip
                  label={device.status}
                  color={
                    device.status === "Healthy"
                      ? "success"
                      : "error"
                  }
                  size="small"
                />

              </TableCell>

            </TableRow>

          ))}

        </TableBody>

      </Table>

    </Paper>
  );
}

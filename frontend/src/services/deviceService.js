import api from "./api";

export async function getDevices() {
  const response = await api.get("/devices/");

  return response.data;
}

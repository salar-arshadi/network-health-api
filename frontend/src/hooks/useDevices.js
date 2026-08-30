import { useEffect, useState } from "react";

import { getDevices } from "../services/deviceService";

export default function useDevices() {

    const [devices, setDevices] = useState([]);

    const [loading, setLoading] = useState(true);

    const [error, setError] = useState("");

    useEffect(() => {

        async function load() {

            try {

                const data = await getDevices();

                setDevices(data);

            } catch (err) {

                console.error(err);

                setError("Unable to load devices.");

            } finally {

                setLoading(false);

            }

        }

        load();

    }, []);

    return {
        devices,
        loading,
        error,
    };

}

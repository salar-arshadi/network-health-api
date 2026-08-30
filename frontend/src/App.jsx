import {
    Routes,
    Route,
    Navigate,
} from "react-router-dom";

import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import DatacenterPage from "./pages/DatacenterPage";

import ProtectedRoute from "./routes/ProtectedRoute";

export default function App() {

    return (

        <Routes>

            <Route
                path="/"
                element={<HomePage />}
            />

            <Route
                path="/login"
                element={<LoginPage />}
            />

            <Route
                path="/datacenter"
                element={

                    <ProtectedRoute>

                        <DatacenterPage />

                    </ProtectedRoute>

                }
            />

            <Route
                path="*"
                element={<Navigate to="/" replace />}
            />

        </Routes>

    );

}

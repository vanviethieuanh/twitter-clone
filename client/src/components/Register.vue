<template>
    <v-container>
        <v-card width="400" class="mx-auto justify-center pa-6" outlined>
            <h1>Register</h1>
            <v-card-text>
                <v-form>
                    <v-row>
                        <v-col>
                            <v-text-field
                                name="f_name"
                                label="First Name"
                                :rules="nameRules"
                                v-model.trim="first_name"
                            ></v-text-field>
                        </v-col>
                        <v-col>
                            <v-text-field
                                name="l_name"
                                label="Last Name"
                                :rules="nameRules"
                                v-model.trim="last_name"
                            ></v-text-field>
                        </v-col>
                    </v-row>

                    <v-text-field
                        v-model.trim="email"
                        label="E-mail"
                        prepend-icon="mdi-email"
                        :rules="emailRules"
                    ></v-text-field>
                    <v-text-field
                        v-model="password"
                        prepend-icon="mdi-lock"
                        name="password"
                        label="Enter your password"
                        :rules="passwordRules"
                        hint="At least 8 characters"
                        min="8"
                        :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                        @click:append="showPassword = !showPassword"
                        :type="showPassword ? 'text' : 'password'"
                    ></v-text-field>
                </v-form>
            </v-card-text>
            <v-card-actions>
                <v-btn
                    color="blue darken-3"
                    depressed
                    text
                    v-on:click="$emit('log-in', $event.target.checked)"
                    >Sign In</v-btn
                >
                <v-spacer></v-spacer>
                <v-btn
                    color="blue"
                    class="ml-2"
                    v-on:click="Register(first_name, last_name, email, password)"
                    depressed
                    dark
                    >Sign Up</v-btn
                >
            </v-card-actions>
        </v-card>
    </v-container>
</template>

<script>
import Authentication from "@/services/auth.js";

export default {
    name: "Register",
    model: {
        event: "log-in",
    },

    data() {
        return {
            first_name: "",
            last_name: "",
            email: "",
            password: "",

            showPassword: false,
            nameRules: [
                (value) => !!value || "Required.",
            ],
            emailRules: [
                (value) => !!value || "Required.",
                (value) => (value || "").length <= 30 || "Max 30 characters",
                (value) => {
                    const pattern = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
                    return pattern.test(value) || "Invalid e-mail.";
                },
            ],
            passwordRules: [
                (value) => !!value || "Required.",
                (value) => (value || "").length >= 8 || "At least 8 characters",
            ],
        };
    },
    methods: {
        async Register() {
            const response = await Authentication.register({
                last_name: this.last_name,
                first_name: this.first_name,
                email: this.email,
                password: this.password,
            });
            response.data.acess
        },
    },
};
</script>

<style lang="scss" scoped>
h1 {
    color: #262626;
    text-align: center;
    font-size: 2.5rem;
    font-family: "Pacifico", cursive;
    font-weight: normal;
}
</style>
